"""
Main application entry point for AI Brick Cement Chatbot
"""
import os
from flask import render_template, request, jsonify, flash, redirect, url_for
from app import create_app

# Create Flask application
app = create_app(os.getenv('FLASK_ENV', 'development'))

# Frontend Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/chat')
def chat():
    """Chat interface page"""
    return render_template('chat.html')

@app.route('/products')
def products():
    """Products page"""
    return render_template('products.html')

@app.route('/orders')
def orders():
    """Orders page"""
    return render_template('orders.html')

@app.route('/quality')
def quality():
    """Quality assessment page"""
    return render_template('quality.html')

@app.route('/admin')
def admin():
    """Admin dashboard page"""
    return render_template('admin.html')

if __name__ == '__main__':
    # Run the application
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )