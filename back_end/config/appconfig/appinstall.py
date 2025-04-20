# Django Rest Framework configuration
from config.appconfig.djangorestframework_config import *

# Django Allauth configuration
from config.appconfig.djangoallauth_config import *

from config.appconfig.phonenumber_field import *

# My app
from config.appconfig.my_app.account_config import *


_VAR = globals()

# Resolve dependece name 
from .utils import find_value
APP_LIST = find_value("_APP_LIST",variables=_VAR)
if APP_LIST is None:
    APP_LIST = []
MIDDLEWARE_APP = find_value("_MIDDLEWARE",variables=_VAR)
if MIDDLEWARE_APP is None:
    MIDDLEWARE_APP = []

CONTEXT_PROCESSORS_LIST = find_value("_CONTEXT_PROCESSOR",variables=_VAR)