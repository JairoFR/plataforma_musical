from flask import Flask
import os
from os.path import join

carpeta = 'static\\uploads'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = join(BASEDIR, carpeta)
ALLOWED_EXTENSIONS = {'mp3', 'jpeg', 'webp', 'jfif', 'gif', 'jpg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ.get("APP_SECRET_KEY")