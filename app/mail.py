#from crypt import methods  #La importacion de este modulo causa conflicto porque no es soportado por windows
from flask import (
    Blueprint, render_template, request
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

        print(name, phone, email, subject, content)
    return render_template('mails/create.html')