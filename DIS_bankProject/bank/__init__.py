from flask import Flask
from flask_bcrypt import Bcrypt
import psycopg2
from flask_login import LoginManager


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = "1237ejkkdsf45lkjsd83123kjbsd"


db = "dbname='bank' user='postgres' host='127.0.0.1' password = 'Magnusniels23'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from .views import views
from .Login.auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')