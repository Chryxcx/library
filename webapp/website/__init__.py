from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from os import pathsep


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SECRET_KEY'] = 'qwertyuiopasdfghjkl;'
    
    from .view import view
    from .auth import auth
    
    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    return app
    
    