import logging

from flask import Flask

logger = logging.getLogger(__name__)

app = Flask(__name__)

DEFAULT_SETTINGS = '{{ app_name }}.config'
app.config.from_object(DEFAULT_SETTINGS)
try:
    app.config.from_envvar('{{ app_name.upper() }}_SETTINGS')
except RuntimeError:
    logger.info('using default settings from {}'.format(DEFAULT_SETTINGS))

from {{ app_name }} import api

__all__ = ['api']
