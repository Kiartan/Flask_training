from flask import Flask, redirect, request, url_for
import os.path

app = Flask(__name__)

content = None

@app.get('/')
def index_get():
    global content
    if content is not None:
        return content
    elif os.path.exists('./test.txt'):
        with open('test.txt', 'r') as f:
            saved_content = f.read()
        if saved_content is not None:
            return saved_content
        else:
            return "<p>Ni ma contynta (None) w test.txt</p>"
    else:
        return "<p>Ni ma test.txt, nic nie wprowadzono na serwer</p>"


@app.post('/')
def savePost():
    global content
    content = request.data.decode("utf-8")
    with open('test.txt', 'w') as f:
        f.write(content)
    return redirect(url_for('index_get'))