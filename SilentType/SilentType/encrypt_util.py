from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key(key):
    return Fernet(key)

def encrypt_data(fernet, data):
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(fernet, token):
    return fernet.decrypt(token.encode()).decode()
