from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User, db
from ..utils.jwt_utils import generate_token
from ..utils.crypto_utils import CryptoUtils
from ..config import Config
from flask_jwt_extended import set_access_cookies, jwt_required
import re

auth_bp = Blueprint('auth', __name__)
crypto = CryptoUtils(Config().ENCRYPTION_KEY)

@auth_bp.route('/verify', methods=['GET'])
@jwt_required()
def verify():
    return jsonify({'message': 'Token is valid'}), 200

# ... rest of the code

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        aadhaar = data.get('aadhaar')

        if not all([name, email, password, aadhaar]):
            return jsonify({'error': 'All fields are required'}), 400

        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            return jsonify({'error': 'Invalid email format'}), 400

        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters'}), 400

        if len(aadhaar) != 12 or not aadhaar.isdigit():
            return jsonify({'error': 'Aadhaar must be 12 digits'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already registered'}), 409

        encrypted_aadhaar = crypto.encrypt(aadhaar)
        password_hash = generate_password_hash(password)

        user = User(name=name, email=email, password_hash=password_hash, aadhaar_encrypted=encrypted_aadhaar)
        db.session.add(user)
        db.session.commit()

        response = jsonify({'message': 'User registered successfully'})
        set_access_cookies(response, generate_token(user.id))
        current_app.logger.info(f"User {user.id} registered successfully")
        return response, 201
    except Exception as e:
        current_app.logger.error(f"Registration error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({'error': 'Email and password are required'}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid credentials'}), 401

        response = jsonify({'message': 'Login successful'})
        set_access_cookies(response, generate_token(user.id))
        current_app.logger.info(f"User {user.id} logged in")
        return response, 200
    except Exception as e:
        current_app.logger.error(f"Login error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500