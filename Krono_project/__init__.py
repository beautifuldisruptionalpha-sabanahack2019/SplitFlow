from flask import Flask
from controller.mysql import MySQLController


app = Flask(__name__)
app.config['SECRET_KEY'] = '983266fff29c2d210fab70ecc474b979'


from Krono_project import routes