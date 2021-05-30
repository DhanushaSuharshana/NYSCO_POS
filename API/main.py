import flask
from flask_mysqldb import MySQL
from flask import request

# Models
from models import user

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nysc_pos'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome, NYSC Point of Sale</h1> "


@app.route('/api/manager/login', methods=['POST'])
def login():
    details = request.form
    result = user.login(mysql, details['username'], details['password'])
    return result


app.run()
