import pytest
from app.utils.crypto_utils import CryptoUtils

def test_encrypt_decrypt():
    key = '0123456789abcdef0123456789abcdef'  # 32 bytes
    crypto = CryptoUtils(key)
    text = '123456789012'
    encrypted = crypto.encrypt(text)
    decrypted = crypto.decrypt(encrypted)
    assert decrypted == text

def test_decrypt_invalid():
    key = '0123456789abcdef0123456789abcdef'
    crypto = CryptoUtils(key)
    with pytest.raises(ValueError):
        crypto.decrypt('invalid_ciphertext')