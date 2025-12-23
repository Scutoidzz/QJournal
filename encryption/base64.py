import base64 as b64

def encrypt_base(text):
    #TODO: Improve the encryption logic
    print("Encrypting...")
    encrypted = b64.b64encode(text.encode()).decode()
    return encrypted