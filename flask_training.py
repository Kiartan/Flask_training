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
    req_id = int(requested_id)
    if os.path.exists('./data.json'):
        with open('data.json', 'r') as f:
           stored_data = json.load(f)
        requested_data = next(iter(item for item in stored_data if item['id'] == req_id), None)
        if requested_data is not None:
            return requested_data
        else:
            return ("<p>Ni ma wpisu o takim id byczq, sprawdź czy się nie machnąłeś</p>")



@app.post('/')
def save_post():
    global content
    content = request.data.decode("utf-8")
    if os.path.exists('./data.json') == False:
        last_id = data_helper.txt_to_json_transformator()
    else: 
        last_id = data_helper.last_id_finder()
    id_new_content = data_helper.json_updater(last_id, content)
    print(id_new_content)
    #return "<p>ID twojego posta to</p>" (id_new_content, redirect(url_for('index_get')))
    #return str(id_new_content)
    return redirect(url_for('index_get'))