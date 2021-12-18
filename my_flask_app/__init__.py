from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "39a9802ccd3e90342235d00d7909c80860cdd728ecf98135"

basedir = os.path.abspath(os.path.dirname(__file__))

print(f"{basedir=}")

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{os.path.join(basedir, 'my_blog_db.db')}"

db = SQLAlchemy(app)

from my_flask_app import routes
