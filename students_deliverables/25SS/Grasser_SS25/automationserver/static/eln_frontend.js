/** Gathers the entered information and sends it to the server, thus saving the notebook
 * 
 * @param {string} url_endpoint: the url endpoint (filled by jinja via url_for)
 */
async function nbSave(url_endpoint){


    let publicprivate = (document.querySelector("select#publicprivate").value == "Public") ? true : false;
    let title = document.querySelector("input#nb-title-input").value;
    let content = document.querySelector("div#nb-content").innerHTML;

    let payload = {
        public: publicprivate,
        title: title,
        content: content
    }

    console.log(payload);
    request = await fetch(url_endpoint, {
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
            "Content-Type":"application/json"
        }
    });

}


/**
 * Switches the detailed notebook view over to edit mode
 */
function nbSwitchToEdit() {

    document.querySelector("button#btn-edit").style.display = "none";
    document.querySelector("button#btn-save").style.display = "inline-block";
    document.querySelector("select#publicprivate").disabled= false;
    document.querySelector("#nb-title").style.display = "none";
    document.querySelector("input#nb-title-input").style.display = "inline-block";
    window.__tinyEditor.transformToEditor(document.querySelector("#nb-content"));
}