import os 

from flask import Flask #Import flask al proyecto

def create_app(): #Punto de partida de la app
    app = Flask(__name__)

#Def variables de entorno con el metodo os.environ de .env y get, el .env es privado y esta reservado, usted debe crear el suyo a la altura de la
#Carpeta madre del proyecto

    app.config.from_mapping( #configuracion de las variables de entorno de la app, configurar .env con ellas
        FROM_EMAIL=os.environ.get('FROM_EMAIL'),
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY'),
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    from.import db #Imortamos las dependencias db con pip

    db.init_app(app)

    from.import mail #Imortamos las dependencias db con pip

    app.register_blueprint(mail.bp) #agregamos blueprint
    
    return app #al final tenemos que retornar la app