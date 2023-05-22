from flask import Flask, redirect, request, url_for
import os.path
import json
from data_helper import DataHelper


app = Flask(__name__)

data_helper = DataHelper()

content = None

@app.get('/')
def index_get():
    global content
    requested_id = request.data.decode("utf-8")
    if requested_id.isnumeric():
        req_id = int(requested_id)
        if os.path.exists('./test.json'):
            requested_data = data_helper.requested_data_finder(req_id)
            if requested_data is not None:
                return requested_data
            else:
                return "<p>Ni ma wpisu o takim id byczq, sprawdź czy się nie machnąłeś</p>"
        else:
            data_helper.txt_to_json_transformator()
            with open('test.json', 'r') as f:
                requested_data = json.load(f)
            return "<p>Jedyny wpis w bazie to: </p>" + str(requested_data)
    else:
        return "<p>ID musi zawierać jedynie cyfry. Chyba coś kombinujesz.</p>"
    



@app.post('/')
def save_post():
    global content
    content = request.data.decode("utf-8")
    if os.path.exists('./test.json'):
        last_id = data_helper.last_id_finder()
    else: 
        last_id = data_helper.txt_to_json_transformator()
    id_new_content = data_helper.json_updater(last_id, content)
    return "<p>ID twojego wpisu to: </p>" + str(id_new_content)