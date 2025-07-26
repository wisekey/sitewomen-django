from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-v1harl$8uh=8v2vzii6nj84lr16(a0v__l#1+s3(uiy0&oboi^'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "sitewomen.ru"]

INTERNAL_IPS = [
    '127.0.0.1',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    'women.apps.WomenConfig',
    "users.apps.UsersConfig",
    "social_django",
    'debug_toolbar',
    "captcha"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'sitewomen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates", 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.get_women_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'sitewomen.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sitewomen_db',
        'USER': 'sitewomen',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "users:login"

AUTHENTICATION_BACKENDS = [
    "social_core.backends.github.GithubOAuth2",
    'social_core.backends.vk.VKOAuth2',
    "django.contrib.auth.backends.ModelBackend",
    "users.authentication.EmailAuthBackend",
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "tembulatbekoff@yandex.ru"
EMAIL_HOST_PASSWORD = "eifjxrlfrmnltkvz"
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

AUTH_USER_MODEL = "users.User"
DEFAULT_USER_IMAGE = "/media/users/default.png"

SOCIAL_AUTH_GITHUB_KEY = 'Ov23liObVBmGTm7wO37K'
SOCIAL_AUTH_GITHUB_SECRET = '15e76072a7a741e3c97393cf83cb3e889bb3dc8c'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'users.pipeline.new_users_handler',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_VK_OAUTH2_KEY = '53965486'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'KO4HN7qeFreHCpYjBbUW'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']