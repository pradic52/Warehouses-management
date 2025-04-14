ALLAUTH_APP_LIST = [
    'allauth',
    'allauth.account',

    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ALLAUTH_CONTEXT_PROCESSOR = ['django.template.context_processors.request']

ALLAUTH_MIDDLEWARE = ["allauth.account.middleware.AccountMiddleware"]

SITE_ID = 1  # requis par django.contrib.sites

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    },
    'facebook': {
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    }
}

# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_LOGIN_METHODS = {"email"}
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
# ACCOUNT_LOGIN_BY_CODE_ENABLED = True
# ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
# ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
# # Pour permettre la connexion avec téléphone en plus (voir section plus bas)
