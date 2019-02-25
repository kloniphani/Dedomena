"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from WebInterface import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/dashboard')
def dashboard():
    """Renders the about page."""
    return render_template(
        'dashboard.html',
        title='Dashboard',
        year=datetime.now().year,
        message_1='Environmental Readings',
        message_2='Acceleration Readings',
        message_3='Orientation Readings'
    )

@app.route('/tracking')
def tracking():
    """Renders the tracking page."""
    return render_template(
        'tracking.html',
        title='Tracking',
        year=datetime.now().year,
        message='Phone Tracking'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Software Developers'
    )
