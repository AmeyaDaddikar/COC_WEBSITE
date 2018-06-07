from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
STATIC_FOLDER = os.getcwd()   + '/App/static'

UPLOAD_FOLDER = STATIC_FOLDER + '/documents'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'csv'])

####### MIGHT BE REQUIRED WHILE FILE HANDLING, ELSE KEEP COMMENTED
# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def read_file(filename):
# 	with open(filename, 'rb') as f:
# 		photo = f.read()
# 	return photo

app = Flask(__name__)
app.secret_key = 'communityofcoders'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coc.db'

db = SQLAlchemy(app)

from . import routes
