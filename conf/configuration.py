import os
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
import django.core.mail.backends.smtp

#############################################
# Django settings for Fidus Writer project. #
#############################################

# After copying this file to configuration.py, adjust the below settings to
# work with your setup.

# If you don't want to show debug messages, set DEBUG to False.

DEBUG = False
# SOURCE_MAPS - allows any value used by webpack devtool
# https://webpack.js.org/configuration/devtool/
# For example
# SOURCE_MAPS = 'cheap-module-source-map' # fast - line numbers only
# SOURCE_MAPS = 'source-map' # slow - line and column number
SOURCE_MAPS = False

SITE_NAME = 'My Fidus Writer ON YUNOHOHOST'
SITE_DOMAIN = '__DOMAIN__'
SITE_URL = 'https://' + SITE_DOMAIN
SECRET_KEY = '__SECRET_KEY__'

MEDIA_ROOT = '__DATA_DIR__/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '__INSTALL_DIR__/static'
STATIC_URL = '/static/'


PROJECT_PATH = os.environ.get("PROJECT_PATH")
# SRC_PATH is the root path of the FW sources.
SRC_PATH = os.environ.get("SRC_PATH")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '__DB_NAME__',
        'USER': '__DB_USER__',
        'PASSWORD': '__DB_PWD__',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 90,
    }
}

# Interval between document saves
DOC_SAVE_INTERVAL = 1

# Migrate, transpile JavaScript and install required fixtures automatically
# when starting runserver. You might want to turn this off on a production
# server. The default is the opposite of DEBUG

# AUTO_SETUP = False

# This determines whether the server is used for testing and will let the
# users know upon signup know that their documents may disappear.
TEST_SERVER = False
# This is the contact email that will be shown in various places all over
# the site.
CONTACT_EMAIL = "__ADMIN_MAIL__"
# Ports that Fidus Writer will run on.
PORTS = [
    __PORT__,
]
#

# Allow the server to listen to all network interfaces (0.0.0.0) instead of just localhost
# SECURITY WARNING: Setting this to True in production environments could expose your server
LISTEN_TO_ALL_INTERFACES = False

ADMINS = (("_ADMIN__", "__ADMIN_MAIL__"),)

# Whether anyone surfing to the site can open an account with a login/password.
REGISTRATION_OPEN = __REGISTRATION_OPEN__

# Whether user's can login using passwords (if not, they will only be able to
# sign in using social accounts).
PASSWORD_LOGIN = True

# Whether anyone surfing to the site can open an account or login with a
# socialaccount.
SOCIALACCOUNT_OPEN = True

# ACCOUNT_EMAIL_VERIFICATION = 'optional'

# This determines whether there is a star labeled "Free" on the login page
IS_FREE = __IS_FREE__

MANAGERS = ADMINS

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "__DOMAIN__"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = "__APP__"
EMAIL_HOST_PASSWORD = "__MAIL_PWD__"
DEFAULT_FROM_EMAIL = "__APP__@__DOMAIN__"
SERVER_EMAIL = "__APP__@__DOMAIN__"

# FOOTER_LINKS = [
#     {
#         "text": "Terms and Conditions",
#         "link": "/pages/terms/"
#     },
#     {
#         "text": "Privacy policy",
#         "link": "/pages/privacy/"
#     },
#     {
#         "text": "Equations and Math with MathLive",
#         "link": "https://github.com/arnog/mathlive#readme",
#         "external": True
#     },
#     {
#         "text": "Citations with Citation Style Language",
#         "link": "https://citationstyles.org/",
#         "external": True
#     },
#     {
#         "text": "Editing with ProseMirror",
#         "link": "https://prosemirror.net/",
#         "external": True
#     }
# ]


INSTALLED_APPS = [
    # If you want to enable one or several of the social network login options
    # below, make sure you add the authorization keys at:
    # http://SERVER.COM/admin/socialaccount/socialapp/
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.stackexchange',
    # "devel",
    "user_template_manager",
]

# A list of apps to remove from the default installation
# This is useful for disabling features you don't need
REMOVED_APPS = [
    # Example: Disable two-factor authentication for admin interface
    # 'django_otp',
    # Example: Disable brute-force protection (for development only)
    # 'axes',
]

# A list of allowed hostnames of this Fidus Writer installation
ALLOWED_HOSTS = [
    "localhost",
    "__DOMAIN__"
]

# Disable service worker (default is True)
# USE_SERVICE_WORKER = False

# The maximum size of user uploaded images in bytes. If you use NGINX, note
# that also it needs to support at least this size.
MEDIA_MAX_SIZE = False

# Create URLs in https (required for social media login)
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

# Which domains served over http to allow post requests from. Should be the same as ALLOWED_HOSTS
# But including https://, for example "https://www.domain.com".
CSRF_TRUSTED_ORIGINS = ["https://__DOMAIN__"]

# Add branding logo inside of "static-libs" folder. For example: static-libs/svg/logo.svg
# BRANDING_LOGO = "svg/logo.svg"

#############################################
# Security Settings                         #
#############################################

# IMPORTANT: For production environments, configure these security settings!

# Enable HTTPS security (required for production)
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS (HTTP Strict Transport Security) - forces HTTPS for your domain
# Only enable this after you're sure HTTPS works correctly!
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

#############################################
# django-axes: Brute-Force Protection      #
#############################################

# django-axes is configured by default with secure settings.
# Customize these if needed:

# Number of failed login attempts before lockout (default: 5)
# AXES_FAILURE_LIMIT = 5

# Lockout duration in hours (default: 1)
# AXES_COOLOFF_TIME = 1

# Lock out parameters by (default: [["ip_address", "user_agent", "username"]])
# AXES_LOCKOUT_PARAMETERS = [["ip_address", "user_agent", "username"]]

# Reset failed attempts after successful login (default: True)
# AXES_RESET_ON_SUCCESS = True

# For deployments behind a proxy/load balancer, ensure IP detection is correct:
# AXES_IPWARE_META_PRECEDENCE_ORDER = [
#     'HTTP_X_FORWARDED_FOR',
#     'REMOTE_ADDR',
# ]

#############################################
# Password Reset Security                   #
#############################################

# Password reset link timeout in seconds
# Default is 24 hours (86400 seconds) for security reasons
# Django's default is 3 days (259200 seconds)
# Recommended: Keep at 24 hours or less for better security
# PASSWORD_RESET_TIMEOUT = 86400  # 24 hours
# PASSWORD_RESET_TIMEOUT = 43200  # 12 hours (more secure)
# PASSWORD_RESET_TIMEOUT = 3600   # 1 hour (very secure)

#############################################
# GDPR Compliance Settings                 #
#############################################

# For GDPR compliance, ensure you have:
# 1. Privacy Policy and Terms of Service (use FOOTER_LINKS or flatpages)
# 2. Cookie consent mechanism (if using tracking cookies)
# 3. Data export functionality for subject access requests
# 4. Data deletion functionality for right to be forgotten
# 5. Contact information for data protection officer (set CONTACT_EMAIL above)

# Session cookie settings (GDPR compliance - user tracking)
# SESSION_COOKIE_AGE = 1209600  # 2 weeks - adjust based on your needs
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# SESSION_SAVE_EVERY_REQUEST = False

# Example footer links with privacy policy and terms:
# FOOTER_LINKS = [
#     {
#         "text": "Privacy Policy",
#         "link": "/pages/privacy/"
#     },
#     {
#         "text": "Terms and Conditions",
#         "link": "/pages/terms/"
#     },
#     {
#         "text": "Data Protection",
#         "link": "/pages/data-protection/"
#     }
# ]

# Email settings for GDPR notifications (e.g., data breach notifications)
# Ensure DEFAULT_FROM_EMAIL and SERVER_EMAIL are properly configured above

# LDAP auth
LDAP_AUTH=1
AUTH_LDAP_SERVER_URI="ldap://localhost:389"
AUTH_LDAP_BIND_DN=""
AUTH_LDAP_BIND_PASSWORD=""
AUTH_LDAP_USER_SEARCH_BASE_DN="ou=users,dc=yunohost,dc=org"
AUTH_LDAP_USER_SEARCH_FILTER_STR="(&(|(objectclass=posixAccount))(uid=%(user)s)(permission=cn=__APP__.main,ou=permission,dc=yunohost,dc=org))"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=users,dc=yunohost,dc=org",
    ldap.SCOPE_SUBTREE,
    "(mail=%(user)s)"
)

# Redis conf
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/__REDIS_DB__',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 50,
            },
            'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
        },
        'TIMEOUT': 300,
    }
}

# Use Redis for sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Authentication
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]