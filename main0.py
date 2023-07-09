'''
Dejo documentado este archivo de las primeras clases
para futuras referencias

'''

from flask import Flask, request, make_response, redirect


app = Flask(__name__)


@app.route('/')
def index():
    mi_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', mi_ip)

    return response


@app.route('/hello')
def hello_world():
    user_ip = request.cookies.get('user_ip')
    return f"<p>Hello World from Flask!!!</p> Tu IP es {user_ip}"
