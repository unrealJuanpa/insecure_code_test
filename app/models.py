class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password  # Almacenamiento en texto plano
        self.email = email
    
    def validate_password(self, input_password):
        # Vulnerable: Comparación directa de strings
        return self.password == input_password