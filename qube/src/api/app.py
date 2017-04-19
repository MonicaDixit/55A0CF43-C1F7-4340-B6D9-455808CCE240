#!/usr/bin/python
"""
Add docstring here
"""
from logging.config import fileConfig
import os

from flask import Flask
from flask_restful_swagger_2 import Api
from pkg_resources import resource_filename
from qube.src.api.helloworld import HelloWorld
from qube.src.commons.log import Log as LOG


logging_config = resource_filename(
    'qube.src.resources', 'logging_config.ini')
fileConfig(logging_config)

app = Flask(__name__)
api = Api(app, api_version='0.1', api_spec_url='/specs')
DEFAULT_HOST = os.environ.get('DEFAULT_LISTENER_HOST', '0.0.0.0')
DEFAULT_PORT = int(os.environ.get('DEFAULT_LISTENER_PORT', '80'))
DEBUG = os.environ.get('DEBUG', 'False') \
    in ("yes", "y", "true", "True", "t", "1")

api.add_resource(HelloWorld, '/<name>')


def main():
    """ main
    """
    app.secret_key = os.urandom(24)
    LOG.info("starting app...")
    app.run(debug=DEBUG,
            host=DEFAULT_HOST,
            port=DEFAULT_PORT)


if __name__ == '__main__':
    main()
