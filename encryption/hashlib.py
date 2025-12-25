import hashlib
import os
import base64
import logging
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Configure logging
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def derive_key(password: str, salt: bytes) -> bytes:
   
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000, # Recommended number of iterations
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    except Exception as e:
        logging.error(f"Error deriving key: {e}")
        raise

def encrypt_text(password: str, text: str) -> str:
    try:
        logging.info("Starting encryption process.")
        
        salt = secrets.token_bytes(16)
        
        # 2. Derive key from password
        key = derive_key(password, salt)
        f = Fernet(key)
        
        # 3. Encrypt the text
        encrypted_data = f.encrypt(text.encode())
        
        # 4. Combine salt and encrypted data for storage (salt + ciphertext)
        # We encode it in base64 to return a clean string
        combined = base64.b64encode(salt + encrypted_data).decode()
        
        logging.info("Encryption successful.")
        return combined
    except Exception as e:
        logging.error(f"Encryption failed: {e}")
        return None

def decrypt_text(password: str, encrypted_combined: str) -> str:
    try:
        data = base64.b64decode(encrypted_combined)
        
        salt = data[:16]
        ciphertext = data[16:]
        
        key = derive_key(password, salt)
        f = Fernet(key)
        
        decrypted_data = f.decrypt(ciphertext)
        return decrypted_data.decode()
    except Exception as e:
        logging.error(f"Decryption failed: {e}")
        return None

def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    # Using scrypt as suggested in TODO
    hashed = hashlib.scrypt(
        password.encode(), 
        salt=salt, 
        n=16384, 
        r=8, 
        p=1
    )
    # Return as salt:hash for storage
    return f"{base64.b64encode(salt).decode()}:{base64.b64encode(hashed).decode()}"

def verify_password(stored_password: str, provided_password: str) -> bool:

    try:
        salt_b64, hash_b64 = stored_password.split(":")
        salt = base64.b64decode(salt_b64)
        stored_hash = base64.b64decode(hash_b64)
        
        new_hash = hashlib.scrypt(
            provided_password.encode(), 
            salt=salt, 
            n=16384, 
            r=8, 
            p=1
        )
        return secrets.compare_digest(stored_hash, new_hash)
    except Exception:
        return False

def encrypt_hashlib(password: str, text: str) -> str:
    return encrypt_text(password, text)
