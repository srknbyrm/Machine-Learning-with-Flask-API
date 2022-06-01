from flask import Flask
from flask_wtf.csrf import CSRFProtect
from views import home, machine_learning_view
from settings import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(app)
    # load default configuration
    app.config.from_object(DevelopmentConfig())
    app.register_blueprint(home.bp)
    app.register_blueprint(machine_learning_view.bp)
    return app


app = create_app()
