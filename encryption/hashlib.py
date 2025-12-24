import hashlib

# TODO: Implement proper cryptographic hash functions
# TODO: Add proper salt and key derivation functions
# TODO: Add proper encryption algorithm selection

def encrypt_hashlib(password, text):
    """
    TODO: Add proper input validation and sanitization
    TODO: Add proper password-based key derivation (PBKDF2, scrypt, Argon2)
    TODO: Add proper error handling and logging
    TODO: Fix function to actually use password for encryption/decryption
    """
    print("Encrypting")
    # TODO: Fix this implementation - currently just hashing text, not encrypting
    # TODO: Add proper salt generation and management
    # TODO: Add proper encryption algorithm (not just hashing)
    hashed = hashlib.sha256(text.encode()).hexdigest()
    password = hashlib.sha256(password.encode()).hexdigest()
    # TODO: This function doesn't actually use the password for encryption
    return hashed
