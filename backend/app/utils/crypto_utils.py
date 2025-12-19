from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

class CryptoUtils:
    def __init__(self, key):
        self.key = key.encode('utf-8') if isinstance(key, str) else key
        if len(self.key) != 32:
            raise ValueError("Encryption key must be 32 bytes for AES-256")

    def encrypt(self, text):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(text.encode('utf-8')) + padder.finalize()
        encrypted = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(iv + encrypted).decode('utf-8')

    def decrypt(self, ciphertext):
        try:
            data = base64.b64decode(ciphertext)
            iv = data[:16]
            encrypted = data[16:]
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()
            decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
            return decrypted.decode('utf-8')
        except Exception as e:
            raise ValueError("Decryption failed") from e