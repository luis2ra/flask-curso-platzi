from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    mi_ip = request.remote_addr
    return f"<p>Hello World from Flask!!!</p> Tu IP es {mi_ip}"
