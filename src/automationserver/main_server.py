"""Main application - a flask server to provide the frontend.

Also provides the simulated pH-Meter with an included SocketIO wrapper for communication"""

import flask
import flask_login
import flask_socketio
import uuid
import automationserver.virtual_phmeter
import pydantic
from typing import Literal, Optional
import requests
import os
import hashlib
from automationserver.eln_server import ELNNotebook
import pathlib
import sqlite3

OWN_PATH = pathlib.Path(__file__)

app = flask.Flask(__file__, static_folder=OWN_PATH.parent /"static", template_folder= OWN_PATH.parent / "templates")
app.config["SECRET_KEY"] = uuid.uuid4().__str__()


# configurations either from env vars for docker or test defaults

ENDPOINT_ELN = ep_eln if (ep_eln := os.environ.get("ENDPOINT_ELN")) else "http://localhost:5001/api/"
"Endpoint for REST requests to the electronic notebook; localhost for local testing, overridden by the image"


# authentication / user management
# no frontend user management - users are stored in `users_db.sqlite`, as username and sha512 hexdigest()

login_manager = flask_login.LoginManager()
login_manager.login_view = ".get_login"
login_manager.init_app(app)

def calc_sha512_hexdigest(password: str) -> str:
    """Hashes the given `password` and returns the SHA512 hexdigest to match against the database"""

    sha = hashlib.sha512()
    sha.update(password.encode())
    return sha.hexdigest()


class User(flask_login.UserMixin):
    """User class, entirely standard from flask_login"""
    def __init__(self, id):
        super().__init__()
        self.id = id

@login_manager.user_loader
def load_user(id):
    return User(id)

def checkUserHasPermission(nb: ELNNotebook, user: User):
    """Checks if the user has permission to view/edit the notebook.
    
    Raises a 401 if they do not"""

    if not (user.id == nb.creator or nb.public):
        flask.abort(401, "Unauthorized for notebook action")

## basic frontend

@app.route("/")
@flask_login.login_required
def get_index():
    return flask.render_template("index.jinja")

@app.route("/login", methods=["GET"])
def get_login():
    """Show the login form"""
    return flask.render_template("login.jinja")

@app.route("/login", methods=["POST"])
def post_login():
    """Authenticate the user vs. the database"""

    print(flask.request.form["user"], flask.request.form["password"])

    db = sqlite3.connect(OWN_PATH.parent / "store/user_db.sqlite", autocommit=True)
    cursor = db.cursor()
    queryres = cursor.execute("SELECT * FROM users WHERE username = ?", (flask.request.form.get("user"),)).fetchone()
    if not queryres: flask.abort(401)
    if not calc_sha512_hexdigest(flask.request.form.get("password")) == queryres[2]: flask.abort(401)
    flask_login.login_user(User(queryres[1]))
    return flask.redirect("/", 301)



# pHmeter control interface and associated websocket handlers
socketio = flask_socketio.SocketIO(app, cors_allowed_origins="*")

pHMeter = automationserver.virtual_phmeter.pHMeter()

class pHMeter_Command_Model(pydantic.BaseModel):
    """JSON validation model for the titration"""
    action: Literal["poll", "add_volume", "reset"]
    volume: Optional[float] = None

@app.route("/phmeter/")
@flask_login.login_required
def get_phmeter_control():
    return flask.render_template("phmetercontrol.jinja")

@socketio.on("phmeter")
def handle_ph_meter(message: dict):

    requestobj = pHMeter_Command_Model.model_validate(message)

    if requestobj.action == "poll":
        flask_socketio.emit("phmeter", {"pH": pHMeter.readout, "volume_added": pHMeter.added_volume_mL})

    elif requestobj.action == "add_volume":
        pHMeter.add(requestobj.volume)
        print("adding ", message.get("volume"), "mL")
        flask_socketio.emit("phmeter", {"pH": pHMeter.readout, "volume_added": pHMeter.added_volume_mL})
    
    elif requestobj.action == "reset":
        pHMeter.__init__()
        flask_socketio.emit("phmeter", {"pH": pHMeter.readout, "volume_added": pHMeter.added_volume_mL})

    else:
        flask_socketio.emit("phmeter", {"status":"warning: could not interpret action!"})
        print("Unknown action - Fallback, this should not be possible")


# Electronic Lab Notebook routes and handlers

def _retrieve_notebook(id: int) -> ELNNotebook:
    """Retrieve a specified notebook from the eln server"""
    notebook_query = requests.get(ENDPOINT_ELN+f"{id}")
    queried_notebook = ELNNotebook.model_validate(notebook_query.json())

    return queried_notebook

@app.route("/eln/")
@flask_login.login_required
def get_eln_index():
    """Query multiple notebooks and display an overview. Requires user to be authorized to view them.
    
    Doubles as search function via query GET argument."""

    payload = {"user":flask_login.current_user.id}

    if (query := flask.request.args.get("query")):
        payload ["query"] = query
        print(payload)
    notebooks_query = requests.post(ENDPOINT_ELN+ "query", json = payload)


    results = [
        {"nb" : (ELNNotebook.model_validate_json(res[1])), "id": res[0]} for res in notebooks_query.json()
    ]
    return flask.render_template("eln_index.jinja", results=results)


@app.route("/eln/<int:id>")
@flask_login.login_required
def get_eln_detailed(id):
    """Get single notebook from the ELN server to view
    
    Checks if the user is authorized to view it (user == current user or the notebook is public), raises a 405 if not"""
    
    nb = _retrieve_notebook(id)
    checkUserHasPermission(nb, flask_login.current_user)
    return flask.render_template("eln_detailed.jinja", nb=nb, id=id)

@flask_login.login_required
@app.route("/eln/new")
def get_eln_new():
    """Frontend action to create a new ELN via PUT request to the ELN server"""
    new_nb = ELNNotebook(
        creator = flask_login.current_user.id,
        public=False,
        title="New Notebook",
        content="Im sad, nothing is written in me.."
    )

    req = requests.put(ENDPOINT_ELN, json=new_nb.model_dump())
    id = req.json().get("id")
    return flask.redirect(flask.url_for("get_eln_detailed", id=id))

@flask_login.login_required
@app.route("/eln/<int:id>/delete")
def get_eln_delete(id):
    "Delete the ELN with this ID, redirect to the overview"

    nb = _retrieve_notebook(id)
    checkUserHasPermission(nb, flask_login.current_user)
    requests.delete(ENDPOINT_ELN + f"{id}")
    return flask.redirect(flask.url_for("get_eln_index"))

@flask_login.login_required
@app.route("/eln/<int:id>/update", methods=["POST"])
def post_eln_update(id):
    """Update the provided ELN. The POST will be passed through to the PATCH method of the ELN in question"""

    nb = _retrieve_notebook(id)
    checkUserHasPermission(nb, flask_login.current_user)

    requests.patch(ENDPOINT_ELN + f"{id}", json=flask.request.json)
    return "saved"

if __name__ == "__main__":
    print(calc_sha512_hexdigest("apikeysarequiteexpensive"))
    socketio.run(app, host="0.0.0.0", allow_unsafe_werkzeug=True)