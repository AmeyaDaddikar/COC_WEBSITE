from flask import render_template, request, flash, redirect, url_for, make_response, session, jsonify
from . import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html')