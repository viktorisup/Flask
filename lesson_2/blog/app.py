from flask import Flask, request, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app
import os

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/blog.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.config["SECRET_KEY"] = "abcdefg123456"


app.register_blueprint(auth_app, url_prefix="/auth")
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin = User(username='admin', is_staff=True)
    vadim = User(username="vadim")

    db.session.add(admin)
    db.session.add(vadim)
    db.session.commit()

    print("created users:", admin, vadim)