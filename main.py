from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER_SECRETO'
# print(app.config)  # veo las variables de configuracion de la instancia de app Flask

todos = ['TODO 1', 'TODO 2', 'TODO 3']


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Enviar')


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
    # response.set_cookie('user_ip', mi_ip)  # quitamos esto pa hacerlo mas seguro
    session['user_ip'] = mi_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    # user_ip = request.cookies.get('user_ip') # lo cambiamos por session
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usario registrado con éxito!')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)  # importante la referencia

'''
Importante la referencia que hace en el pase de esta variable **context,
que python utiliza para expandir las variables

Opcionalmente, se puede haber manejado con la sintaxix context=context
'''
