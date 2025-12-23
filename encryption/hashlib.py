import hashlib

def encrypt_hashlib(password, text):
    #TODO: Add password encryption
    print("Encrypting")
    hashed = hashlib.sha256(text.encode()).hexdigest()
    return hashed
