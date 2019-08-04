import os

from flask import render_template, url_for, flash, redirect, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from Krono_project import app, excel_to_json, ALLOWED_EXTENSIONS, CORS


def allowed_file(filename):
    return filename.split(".")[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print (request.files)
        if 'file' not in request.files:
            return 'No hay respuesta'
        archivo = request.files['file']
        if archivo and allowed_file(archivo.filename):
            print('found file', archivo.filename)
            filename = secure_filename(archivo.filename)
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            archivo.save(filename)
            a = excel_to_json(filename)
            b = a.return_json()
            print (b)
            return b
        else:
            return "errorororoeroeroe"
    return url_for('index')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/')
def index():
    return 'Hola'

