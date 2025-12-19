# Secure User Profile & Access Control System

## Project Overview

This is a full-stack web application implementing a secure user profile and access control system. The backend is built with Flask and PostgreSQL, featuring JWT authentication, bcrypt password hashing, and AES-256 encryption for sensitive data like Aadhaar numbers. The frontend is developed using React with Tailwind CSS for a clean, responsive UI.

## Tech Stack

- **Backend**: Flask, PostgreSQL, SQLAlchemy, JWT (Flask-JWT-Extended), bcrypt, cryptography (AES-256)
- **Frontend**: React, Tailwind CSS, Axios, React Router
- **Testing**: pytest
- **Deployment**: Monorepo structure for easy development

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL
- pip and npm

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env` file and update with your values:
     ```
     SECRET_KEY=your-secret-key
     DATABASE_URL=postgresql://username:password@localhost/lenden_db
     JWT_SECRET_KEY=your-jwt-secret
     ENCRYPTION_KEY=32-character-encryption-key
     ```

5. Create the database:
   ```bash
   createdb lenden_db  # Or use your preferred method
   ```

6. Run the application:
   ```bash
   python run.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser to `http://localhost:5173`

### Running Tests

For backend tests:
```bash
cd backend
pytest
```

## API Documentation

### Authentication Endpoints

#### POST /api/auth/register
Register a new user.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword",
  "aadhaar": "123456789012"
}
```

**Response:**
```json
{
  "message": "User registered successfully",
  "token": "jwt-token-here"
}
```

#### POST /api/auth/login
Authenticate a user.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "token": "jwt-token-here"
}
```

### Profile Endpoint

#### GET /api/profile
Retrieve user profile (requires JWT token in Authorization header).

**Response:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "aadhaar": "123456789012"
}
```

## Database Schema

### User Table

| Column          | Type      | Constraints          |
|-----------------|-----------|----------------------|
| id              | UUID      | Primary Key          |
| name            | VARCHAR   | Not Null             |
| email           | VARCHAR   | Unique, Not Null     |
| password_hash   | VARCHAR   | Not Null             |
| aadhaar_encrypted| TEXT     | Not Null             |
| created_at      | TIMESTAMP | Default: Current Time|

## Security Features

- **Password Hashing**: Uses bcrypt for secure password storage.
- **JWT Authentication**: Stateless authentication with access tokens stored in httpOnly cookies.
- **Data Encryption**: Aadhaar numbers are encrypted using AES-256 before storage.
- **Input Validation**: Server-side validation for all user inputs.
- **CORS Enabled**: Configured for cross-origin requests.
- **Error Handling**: Proper error responses without exposing sensitive information.
- **Logging**: Structured logging for debugging and monitoring.

## Recent Fixes and Improvements

Based on a senior full-stack audit, the following fixes were implemented:

- **CORS Setup**: Added Flask-CORS to enable cross-origin requests from the frontend.
- **Secure Token Storage**: Switched from localStorage to httpOnly cookies for JWT tokens to prevent XSS attacks.
- **Auth State Management**: Implemented React Context for centralized authentication state.
- **Error Logging**: Added logging to backend routes for better debugging.
- **Token Validation**: Added `/api/auth/verify` endpoint for proactive token validation.
- **Configurable API Base URL**: Made backend URL configurable via environment variables.
- **Test Updates**: Updated tests to validate cookie-based authentication.

These changes enhance security, reliability, and maintainability of the application.

## AI Tool Usage Log

### Tools Used
- **GitHub Copilot**: Assisted in generating boilerplate code for Flask routes, React components, and Tailwind CSS styling. Also helped in implementing fixes like CORS, cookie-based auth, and context management.
- **Code Completion**: Used for rapid prototyping of API endpoints and frontend forms.
- **Documentation Generation**: Helped in creating comprehensive README and inline comments.
- **Audit and Fixes**: Provided detailed audit feedback and guided implementation of security and reliability improvements.

### Effectiveness Score: 5/5
**Justification**: GitHub Copilot significantly accelerated development by providing accurate code snippets for common patterns like JWT implementation, React hooks, and SQLAlchemy models. It reduced boilerplate code writing by ~60%, allowing focus on business logic and security implementation. The AI also assisted in identifying and fixing critical issues like CORS and token security, making the application production-ready. Highly effective for both initial development and iterative improvements.