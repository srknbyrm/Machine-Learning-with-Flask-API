from flask import Flask
from flask_wtf.csrf import CSRFProtect
from views import machine_learning_view
from settings import DevelopmentConfig

def create_app(config=None):
    app = Flask(__name__)
    app.debug = True

    # load default configuration
    app.config.from_object(DevelopmentConfig())

    app.register_blueprint(machine_learning_view.bp)
    return app


app = create_app()
