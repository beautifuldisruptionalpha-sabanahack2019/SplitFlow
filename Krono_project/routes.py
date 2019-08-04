import os

from flask import render_template, url_for, flash, redirect, request, jsonify
from Krono_project import app

@app.route('/')
def index():
    return render_template('index.html')
