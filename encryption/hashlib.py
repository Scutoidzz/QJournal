import hashlib

def encrypt_hashlib(password, text):
    print("Encrypting")
    hashed = hashlib.sha256(text.encode()).hexdigest()
    return hashed
