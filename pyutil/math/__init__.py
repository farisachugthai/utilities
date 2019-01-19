import logging
from logging import NullHandler
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
logging.getLogger(__name__).addHandler(NullHandler())
