from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.route('/')
def index():
    mi_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', mi_ip)

    return response


@app.route('/hello')
def hello_world():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)  # importante la referencia

'''
Importante la referencia que hace en el pase de esta variable **context,
que python utiliza para expandir las variables

Opcionalmente, se puede haber manejado con la sintaxix context=context
'''
