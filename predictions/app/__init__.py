from flask import Flask
from app.config import Config
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.config.from_object(Config)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

from app import routes