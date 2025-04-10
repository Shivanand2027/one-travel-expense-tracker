from functools import wraps
from flask import request, jsonify
from app import app

def greeting_middleware():
    @wraps(app.route)
    def middleware():
        if request.path == '/welcome':
            # In a real application, you would fetch this from your configuration
            # For demonstration, we'll use a static greeting
            greeting = {"message": "Welcome to the Travel Expense App!"}
            return jsonify(greeting)
        return None
    
    return app.before_request(middleware)

# Initialize the middleware
greeting_middleware()