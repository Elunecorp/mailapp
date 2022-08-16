instructions = [
    'DROP TABLE IF EXISTS email;',

    """
        CREATE TABLE IF NOT EXISTS email (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            email VARCHAR(100) NOT NULL,
            phone VARCHAR(25) NOT NULL,
            subject VARCHAR(50) NOT NULL,
            content VARCHAR(256) NOT NULL
        );
    """
]