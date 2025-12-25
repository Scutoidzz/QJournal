import base64 as b64
import logging
def encrypt_base(text):
    logging.log(logging.INFO, "Encrypting...")

    try:
        encrypted = b64.b64encode(text.encode()).decode()
    except Exception as e:
        logging.log(logging.ERROR, f"Error encrypting text: {e}")
        return None
    return encrypted