"""Basic CRUD application handling electronic lab notebook entries

Designed to run as seperate application from the frontend, not accessible from outside but only inside the container network.
By this token, user authentication and privilege management is handled by the frontend."""


import pydantic
import flask
from flask.views import MethodView
import datetime
from typing import Literal
import sqlite3
import pathlib
from typing import Optional
import json



# Model definitions

app = flask.Flask(__file__)

class ELNFile(pydantic.BaseModel):
    """Basic Metadata needed to be contained in every ELN data section"""
    creator: str
    """The creator's user ID"""
    timestamp: datetime.datetime
    """Creation Timestamp"""
    name: str
    """filename as uploaded"""
    uuid: str
    """UUID used as filename"""


class ELNNotebook(pydantic.BaseModel):
    """A complete electronic lab notebook entry, composed of individual data sections"""

    creator: str
    """The owner's user ID"""
    public: bool = False
    """Whether or not the notebook (and its entries) are public"""
    title: str
    """Short title/description for indexes, searches and the like"""
    content: str
    """HTML content forming the main body of the notebook"""
    tags: list[str] = []
    """List of tags applying to the entry"""
    files: list[ELNFile] = []
    """Uploaded files attached to the notebook"""



# Define APIs and Routes

class API_ELN(MethodView):
    """CRUD implementation of a single ELN entry. `ELNData` entries have no seperate API, but are necessarily always connected
    to their containing `ELNNotebook` entry
    
    Supports `PUT`, `GET`, `DELETE`, `PATCH` (and implicitly `OPTIONS`)"""
    
    init_every_request = False

    def get(self, id):
        """Retrieve ELN entry with `id` as dict or JSON if view
        
        Returns:
            the JSON of the fetched entry (or a 404)"""
        
        db = sqlite3.connect(DB_PATH, autocommit=True)
        cursor = db.cursor()
        cursor.execute("SELECT json FROM electronic_lab_notes WHERE id = ?", (id,))
        
        fetchres = cursor.fetchone()
        cursor.close()
        db.close()
        if not fetchres: flask.abort(404, "The requested resource was not found")
        nb = ELNNotebook.model_validate_json(fetchres[0])
        return nb.model_dump()
    
    def put(self, id="new"):
        """Create a new ELN entry. An ID is not necessary and will be ignored (one will be assigned automatically)
        
        Returns:
            A JSON with `id:<int>` - the ID of the newly created entry"""
        
        print("PUT request for ID")
        json_data = flask.request.json
        try:
            validated = ELNNotebook.model_validate(json_data)
        except pydantic.ValidationError:
            flask.abort(415, "JSON did not pass validation")

        db = sqlite3.connect(DB_PATH, autocommit=True)
        cursor = db.cursor()
        cursor.execute("INSERT INTO electronic_lab_notes(json) VALUES (?)",
                       (validated.model_dump_json(),))
        cursor.close()
        db.close()

        return {"id":cursor.lastrowid}
    
    def patch(self, id):
        """"Update the existing ELN entry with `<id>`. Allows partial JSONs of the ELN Notebook"""
        
        old_model:dict = self.get(id)
        print("old", old_model)
        json_data = flask.request.json
        print("json", json_data)
        new_model = ELNNotebook.model_validate(dict(old_model, **json_data))

        db = sqlite3.connect(DB_PATH, autocommit=True)
        cursor = db.cursor()
        cursor.execute("UPDATE electronic_lab_notes SET json=? WHERE id = ?", (new_model.model_dump_json(), id))
        cursor.close()
        db.close()
        
        return new_model.model_dump()
    

    def delete(self, id):
        """Delete ELN item with `<id>`"""

        db = sqlite3.connect(DB_PATH, autocommit=True)
        cursor = db.cursor()
        cursor.execute("DELETE FROM electronic_lab_notes WHERE id = ?", (id,))
        cursor.close()
        db.close()

        response = flask.make_response()
        response.status_code = 200
        return response

app.add_url_rule("/api/", view_func=API_ELN.as_view("API_ELN_PUT"))
app.add_url_rule("/api/<int:id>", view_func=API_ELN.as_view("API_ELN"))

class QueryModel(pydantic.BaseModel):
    "The model for JSON queries submitted to the search function"
    user: Optional[str] = None
    """Limit the query to entries visible to this user (own or public). If None, returns all entries"""
    query: Optional[str] = None
    """The query. If None, return all entries. If present, match against tags and content and only return matching notebooks"""

@app.route("/api/query", methods=["POST"])
def post_query_eln():
    """Query the ELN server and return matching notebooks
    
    Payload:
        A JSON compliant with the `QueryModel`
    Returns:
        A JSON list of `ELNNotebook` instances"""
    
    query = QueryModel.model_validate(flask.request.json)

    db = sqlite3.connect(DB_PATH, autocommit=True)
    cursor = db.cursor()

    if query.user and not query.query:
        cursor.execute("""SELECT id,json FROM electronic_lab_notes WHERE (json_extract(json, "$.public") = true OR json_extract(json, "$.creator") = ?)""", (query.user,))
    elif query.user and query.query:
        cursor.execute("""SELECT id,json FROM electronic_lab_notes WHERE (json_extract(json, "$.public") = true OR json_extract(json, "$.creator") = ?) AND json LIKE ?""", (query.user,f"%{query.query}%"))
    elif query.query:
        cursor.execute("""SELECT id,json FROM electronic_lab_notes WHERE json LIKE %?%""", (query.user,query.query))
    
    queryres = cursor.fetchall()
    cursor.close()
    db.close()

    return queryres

if __name__ == "__main__":
    # Establish database connection and, if necessary, scheme
    DB_PATH = pathlib.Path(__file__).parent / "store" / "eln_db.sqlite"
    print("Connecting to db", DB_PATH)
    db = sqlite3.connect(DB_PATH, autocommit=True)

    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS electronic_lab_notes(id INTEGER PRIMARY KEY, json TEXT)""")
    cursor.close()
    db.close()


    app.run(port=5001, host="0.0.0.0")