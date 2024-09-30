import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://uthzadp7pqx:o4lVcCpp3At1@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech/poker_polar_trick_817030", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)

from taskmanager import routes  # noqa