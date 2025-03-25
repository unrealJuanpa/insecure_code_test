from flask import Flask
from app.routes import app as application

if __name__ == '__main__':
    # Vulnerable: Modo debug activado, escucha en todas las interfaces
    application.run(host='0.0.0.0', port=5000, debug=True)