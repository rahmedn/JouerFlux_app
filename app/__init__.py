from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flasgger import Swagger
from flask import jsonify
import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_name)
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    setup_logging(app)

    from .routes.firewall_routes import firewall_blueprint
    from .routes.policy_routes import policy_blueprint
    from .routes.rule_routes import rule_blueprint

    app.register_blueprint(firewall_blueprint, url_prefix='/api')
    app.register_blueprint(policy_blueprint, url_prefix='/api')
    app.register_blueprint(rule_blueprint, url_prefix='/api')

    Swagger(app, template_file='static/swagger.json')

    @app.route('/swagger.json')
    def swagger_json():
        return jsonify(app.config['SWAGGER'])

    return app


def setup_logging(app):
    log_file = app.config.get('LOG_FILE', 'logs/myapp.log')
    log_level = app.config.get('LOG_LEVEL', logging.DEBUG)
    log_format = app.config.get('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(log_format))

    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)
