from flask import Flask, redirect, request, url_for
import os.path
import json
from data_helper import *


app = Flask(__name__)


content = None

@app.get('/')
def index_get():
    global content
    requested_id = request.data.decode("utf-8")
    if requested_id.isnumeric():
        req_id = int(requested_id)
        if os.path.exists('./test.json'):
            requested_data = find_requested_data(req_id)
            if requested_data is not None:
                return requested_data
            else:
                return "<p>Ni ma wpisu o takim id byczq, sprawdź czy się nie machnąłeś</p>"
        else:
            transform_txt_to_json()
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
        last_id = find_last_id()
    else: 
        last_id = transform_txt_to_json()
    id_new_content = update_json(last_id, content)
    return "<p>ID twojego wpisu to: </p>" + str(id_new_content)