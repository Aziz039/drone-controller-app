'''
This is a centralized configuration settings for the Flask web application.
It's like a guidance book that tells the application where things are.
It defines parameters like the web address, port, file paths, 
and debugging options, providing a consistent configuration across the application.
'''

import os

from flask import Flask


WEB_ADDRESS = '0.0.0.0'
WEB_PORT = 2030
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(PROJECT_ROOT, 'droneapp/templates')
STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'droneapp/static')
DEBUG = False
LOG_FILE = 'pytello.log'

app = Flask(__name__,
            template_folder=TEMPLATES,
            static_folder=STATIC_FOLDER)
if DEBUG:
    app.debug = DEBUG
