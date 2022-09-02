#from crypt import methods  #La importacion de este modulo causa conflicto porque no es soportado por windows
from contextlib import redirect_stderr
from flask import (
    Blueprint, render_template, request, flash, url_for, redirect, current_app
)

import sendgrid
from sendgrid.helpers.mail import *

from app.db import get_db

bp = Blueprint('mail', __name__, url_prefix="/")

@bp.route('/', methods=['GET'])
def index():

    search = request.args.get('search')
    #print(search) print en consola para comprobar que recibe el string

    db, c = get_db()

    if search is None: #Si el contenido en la variable search o campo de busqueda esta limpio 
        c.execute("SELECT * FROM email") #entonces solo mostrar la lista de todos los email
    else:
        c.execute("SELECT * FROM email WHERE  email like %s", ('%' + search + '%', )) #Mostra las coincidencias de la columna de email omitiendo los espacios

    mails = c.fetchall()

    # print(mails) #print para mostrar correos en la terminal flask run

    return render_template('mails/index.html', mails=mails)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        #name = request.form.get('name')
        #phone = request.form.get('phone')
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []

        # if not name:
        #     errors.append("El Nombre es obligatorio")
        #if not phone:
        #    errors.append("El Número de Telefono o WhatsApp es obligatorio")
        if not email:        #Condicion para que los campos sean obligatorios y no dejarlos vacios
            errors.append("Email es obligatorio")
        if not subject:
            errors.append("El Asunto del correo es obligatorio")
        if not content:
            errors.append("El Contenido del correo es obligatorio")

        #print(name, phone, email, subject, content)
        #print(errors)

        if len(errors) == 0:
            send(email, subject, content)
            db, c = get_db()
            c.execute("INSERT INTO email (email, subject, content) VALUES (%s, %s, %s)", (email, subject, content))
            db.commit()

            return redirect(url_for('mail.index'))
        else:
            for error in errors:
                flash(error)
    return render_template('mails/create.html')

def send(to, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
    from_email = Email(current_app.config['FROM_EMAIL'])
    to_email = To(to)
    content = Content('text/plain', content)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response)