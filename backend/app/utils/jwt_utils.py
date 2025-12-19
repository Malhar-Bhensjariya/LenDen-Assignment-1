# JWT utilities using flask-jwt-extended
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def generate_token(identity):
    return create_access_token(identity=identity)

def get_current_user():
    return get_jwt_identity()