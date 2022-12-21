from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0'
]

try:
    from .local import *
except ImportError:
    pass
