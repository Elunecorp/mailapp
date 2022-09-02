instructions = [
    'DROP TABLE IF EXISTS email;',

    """
        CREATE TABLE IF NOT EXISTS email (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            email VARCHAR(100) NOT NULL,
            subject VARCHAR(50) NOT NULL,
            content VARCHAR(256) NOT NULL
        );
    """
]

#archivo conf con las instrucciones para la db
#Las credenciales de la db son privadas y estan en el .env que se debe crear