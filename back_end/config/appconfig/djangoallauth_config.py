from config.env import env
ALLAUTH_APP_LIST = [
    
    # django-allauth et extensions
    "allauth",
    "allauth.account",                   # gestion des comptes (inscription, login, etc.)
    "allauth.socialaccount",             # connexion via réseaux sociaux
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "allauth.mfa",                       # authentification à facteurs multiples
    "allauth.headless",                  # mode sans templates HTML intégrés
    "allauth.usersessions",              # gestion fine des sessions utilisateur
]

ALLAUTH_MIDDLEWARE = ["allauth.account.middleware.AccountMiddleware",]
# allauth settings
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_METHODS = {"email", "phone"}

ACCOUNT_PHONE_VERIFICATION_ENABLED = True

ACCOUNT_PHONE_VERIFICATION_MAX_ATTEMPTS = 5
ACCOUNT_PHONE_VERIFICATION_TIMEOUT = 900  # en secondes
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
ACCOUNT_SIGNUP_FIELDS = ["phone*", "email*", "password1*", "password2*"]
ACCOUNT_ADAPTER = "account_config.adapter.CustomAccountAdapter"
ACCOUNT_CHANGE_EMAIL = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[ALB]"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
ACCOUNT_EMAIL_NOTIFICATIONS = True

if env("DJANGO_SETTINGS_MODULE") == "config.django.production":
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"


SITE_ID = 1

# headless / API only
HEADLESS_ONLY = True
HEADLESS_FRONTEND_URLS = {
    "account_confirm_email": "/account/verify-email/{key}",
    "account_reset_password": "/account/password/reset",
    "account_reset_password_from_key": "/account/password/reset/key/{key}",
    "account_signup": "/account/signup",
    "socialaccount_login_error": "/account/provider/callback",
}
HEADLESS_SERVE_SPECIFICATION = True


# MFA
MFA_SUPPORTED_TYPES = ["totp", "recovery_codes", "webauthn"]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = True