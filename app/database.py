import sqlite3
from config import Config

def init_db():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cursor = conn.cursor()
    
    # Vulnerable: No preparación de statements
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT,
            is_admin INTEGER DEFAULT 0
        )
    ''')
    
    # Vulnerable: Inserción directa sin hash de contraseña
    cursor.execute('''
        INSERT OR IGNORE INTO users 
        (username, password, email, is_admin) VALUES 
        ('admin', 'admin123', 'admin@local.com', 1)
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    # Vulnerable: Conexión sin gestión de excepciones
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn