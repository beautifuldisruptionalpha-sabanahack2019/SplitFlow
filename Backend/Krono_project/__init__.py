from flask import Flask
from flask_cors import CORS
from controller.excel import excel_to_json

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['xlsx'])

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '983266fff29c2d210fab70ecc474b979'


from Krono_project import routes