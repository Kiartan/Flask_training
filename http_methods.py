from flask import Flask, redirect, request, url_for


app = Flask(__name__)


content = None

@app.get("/")
def index_get():
    global content
    if content is not None:
        return content
    return "<p>Kontent był nullem (None)</p>"

@app.post("/")
def index_post():
    global content
    content = request.data.decode("utf-8")
    return redirect(url_for('index_get'))
    