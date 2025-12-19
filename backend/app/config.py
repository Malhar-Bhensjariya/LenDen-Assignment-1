import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
        if os.getenv('TESTING') == 'True':
            self.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        else:
            self.SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/lenden_db')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
        self.ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', 'default-encryption-key-32-chars!')