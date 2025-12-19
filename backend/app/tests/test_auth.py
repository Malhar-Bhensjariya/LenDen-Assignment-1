import pytest
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    import os
    os.environ['TESTING'] = 'True'
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_register(client):
    response = client.post('/api/auth/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123',
        'aadhaar': '123456789012'
    })
    assert response.status_code == 201
    assert 'access_token_cookie' in response.headers.get('Set-Cookie', '')

def test_login(client):
    # First register
    client.post('/api/auth/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123',
        'aadhaar': '123456789012'
    })
    # Then login
    response = client.post('/api/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'access_token_cookie' in response.headers.get('Set-Cookie', '')