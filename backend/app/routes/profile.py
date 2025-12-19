from flask import Blueprint, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import User
from ..utils.crypto_utils import CryptoUtils
from ..config import Config

profile_bp = Blueprint('profile', __name__)
crypto = CryptoUtils(Config().ENCRYPTION_KEY)

@profile_bp.route('', methods=['GET'])
@jwt_required()
def get_profile():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        try:
            aadhaar = crypto.decrypt(user.aadhaar_encrypted)
        except ValueError:
            current_app.logger.error(f"Decryption failed for user {user_id}")
            return jsonify({'error': 'Failed to decrypt Aadhaar'}), 500

        current_app.logger.info(f"Profile accessed for user {user_id}")
        return jsonify({
            'name': user.name,
            'email': user.email,
            'aadhaar': aadhaar
        }), 200
    except Exception as e:
        current_app.logger.error(f"Profile error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500