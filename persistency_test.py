from flask import Flask, redirect, request, url_for

app = Flask(__name__)

content = None

@app.get('/')
def index_get():
    global content
    with open('test.txt', 'r') as f:
        saved_content = f.read()
        f.close()
    if saved_content is not None:
        return saved_content
    return "<p>Ni ma contynta (None)</p>"


@app.post('/')
def savePost():
    global content
    content = request.data.decode("utf-8")
    with open('test.txt', 'a') as f:
        f.write(content)
        f.close()
    return redirect(url_for('index_get'))