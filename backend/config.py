from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import sentry_sdk
import logging
from prometheus_flask_exporter import PrometheusMetrics


sentry_sdk.init(
    dsn="https://fb37f9458dde56eba5c6a3d7e6ed1781@o4507126885711872.ingest.us.sentry.io/4507126979559424",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

app = Flask(__name__)
CORS(app)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)