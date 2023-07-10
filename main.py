from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

todos = ['TODO 1', 'TODO 2', 'TODO 3']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    '''
    Esto permite simular un error 500 en el servidor
    Nota: para probarlo en local, hay que desactivar 
    la opcion debug al iniciar el servidor de flask
    '''
    # raise Exception("Error 500 - Internal Server Error")
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
