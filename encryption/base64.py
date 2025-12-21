import base64 as b64

def encrypt_base(text):
    print("Encrypting...")
    encrypted = b64.b64encode(text.encode()).decode()
    return encrypted