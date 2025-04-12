# Django Rest Framework configuration
from config.appconfig.djangorestframework import *
# Django Allauth configuration
# from config.appconfig.djangoallauth import *




# Resolve dependece name 
from utils import find_value
APP_LIST = [
    find_value("APP_LIST")
    
]

MIDDLEWARE_APP = []

CONTEXT_PROCESSORS_LIST = []