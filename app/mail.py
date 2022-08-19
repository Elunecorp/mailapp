#from crypt import methods  #La importacion de este modulo causa conflicto porque no es soportado por windows
from flask import (
    Blueprint, render_template, request, flash
)

from app.db import get_db

bp = Blueprint('mail', __name__, url_prefix="/")

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()

    c.execute("SELECT * FROM email")
    mails = c.fetchall()

    # print(mails) #print para mostrar correos en la terminal flask run

    return render_template('mails/index.html', mails=mails)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []

        if not name:
            errors.append("El Nombre es obligatorio")
        if not phone:
            errors.append("El Número de Telefono o WhatsApp es obligatorio")
        if not email:
            errors.append("Email es obligatorio")
        if not subject:
            errors.append("El Asunto del correo es obligatorio")
        if content:
            errors.append("El Contenido del correo es obligatorio")

        #print(name, phone, email, subject, content)
        #print(errors)

        if len(errors) == 0:
            pass
        else:
            for error in errors:
                flash(error)
    return render_template('mails/create.html')