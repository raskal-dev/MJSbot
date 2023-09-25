from gevent import monkey

monkey.patch_all()
def create_app():
    """
    creation application flask
    :return instance application
    """
    from flask import Flask
    from config import logger,Config
    app = Flask(__name__)
    _configure_blueprints(app)
    logger.info(Config.MESSAGE_LOGIN)

    return app
def _configure_blueprints(app):
    """
    configuration bot application
    :param app: instance application Flask
    """
    from bot import pharmacy_guard

    blueprints = [
        pharmacy_guard,
    ]
    for route in blueprints:
        app.register_blueprint(route)
