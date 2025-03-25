class Config:
    SECRET_KEY = 'very-weak-secret-key-that-is-hardcoded'
    DATABASE_PATH = 'users.db'
    DEBUG = True  # Expone información detallada de errores
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # Innecesario y potencialmente inseguro