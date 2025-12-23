import hashlib

def encrypt_hashlib(password, text):
    print("Encrypting")
    hashed = hashlib.sha256(text.encode()).hexdigest()
    password = hashlib.sha256(password.encode()).hexdigest()
    return hashed
