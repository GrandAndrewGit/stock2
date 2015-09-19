# -*- coding: utf-8 -*-

##
##------------------------------------------------------------##
import sys

default_hold = 36 ##default withdraw hold

PROJECT_NAME="BITCOIN TRADE COMPANY"
ADMIN_TOOLS_INDEX_DASHBOARD = 'crypton.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'crypton.dashboard.CustomAppIndexDashboard'


BASE_URL = "https://bitmoney.trade/"
BASE_HOST = "bitmoney.trade"

COMISSION_USER = 2
CRYPTO_USER = 3
DEFAULT_CHARSET ="utf-8"

LIQPAY_MERCHID="i4196993"
LIQPAY_KEY="rTr98EffzI2N"


P24_MERCHID="110548"
P24_PASSWD="7kzW4vSUHKwE1DSNd78s21FQBOzk521u"
P24MERCH_CARD="5218575700001652"

BANK_UAH_OKPO = "12312"
BANK_UAH_MFO = "12312211"
BANK_UAH_ACCOUNT = "123123112"
BANK_USER = 6
BANK_KEY_SALT = "bank_key_salt_depost_hui_hui"


UNIQ_CHECK_SIGN = "88m_lUNIQ_CHECK_SIGN_sd$asa"
UNIQ_CHECK_URL = "http://127.0.0.1:8013/app/check"



AES_KEY1 = "AES_KEY1"
AES_IV = "AES_KEY1"


## for pin auth
PIN_SALT = "ss2-34i23omnxnvkjnos;lrk[2o-=3orks;ldkmf"
PIN_URL_CHECK = "http://127.0.0.1:8070/codes/check/31/"
PIN_SIGNATURE = "#we_45tlsnlsdfS_sdfsdg"



SIGN_SALT = "sadfsdfsdfs"
COMMON_SALT = "sdfsd_DSfs"
CRYPTO_SALT = "test"


ROOT_PATH = "/home/btctrade/stock/"

DEBUG = True
TEMPLATE_DEBUG = DEBUG
USE_X_FORWARDED_HOST=True
ALLOWED_HOSTS=[ "52.28.243.121","127.0.0.1","ttt.btc-trade.com.ua","localhost","127.0.0.1:8366" ]

HELPDESK_FOOTER_SHOW_CHANGE_LANGUAGE_LINK = True
HELPDESK_FOOTER_SHOW_API_LINK = False
HELPDESK_ALLOW_NON_STAFF_TICKET_UPDATE = False
HELPDESK_SUPPORT_PERSON = "perldev@mail.ru"
HELPDESK_KB_ENABLED = False
HELPDESK_DEFAULT_SETTINGS = {
        'use_email_as_submitter': True,
        'email_on_ticket_assign': True,
        'email_on_ticket_change': True,
        'login_view_ticketlist': True,
        'email_on_ticket_apichange': True,
        'tickets_per_page': 25
        }

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = (
            global_settings.TEMPLATE_CONTEXT_PROCESSORS +
            ('django.core.context_processors.request','django.core.context_processors.i18n')
     )
MIN_CONFIRM = 7

ADMINS = (
     ('BTC TRADE UA Admin', 'btctradeua@gmail.com'),
)

ADMIN_COPY = 'btctradeua@gmail.com'

TRANS_PREC = 10

#EMAIL_HOST = "127.0.0.1"
#EMAIL_PORT = "25"
#EMAIL_HOST_USER = "robot@btc-trade.com.ua"
#EMAIL_HOST_PASSWORD = None #"#hervam210286"

DEFAULT_FROM_EMAIL= "robot@btc-trade.com.ua"  #"btctradeua@gmail.com" # "django@btc-trade.com.ua"

EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT=587 #465
EMAIL_HOST_USER = "robot@btc-trade.com.ua"
EMAIL_HOST_PASSWORD = "randomnumber66" #"#hervam2106"
EMAIL_USE_TLS = True
#EMAIL_USE_SSL =  True
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = PROJECT_NAME
SERVER_EMAIL = "robot@btc-trade.com.ua"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


SERVER_EMAIL ="server@btc-trade.com.ua"

help_page = u"Помощь"
pin_page= u"Страница персонального PIN кода"
pagetitle_main = PROJECT_NAME
pagetitle_home = u""
withdraw_cancel = u"Вывод отменен"
withdraw_msg_cancel = u"Ваша заявка на вывод отменена, мы рады, что вы остаетесь с нами"

secondary_main = PROJECT_NAME
secondary_regis = u"Регистрация"
secondary_regis_success = u"Регистрация прошла успешно"
secondary_regis_finish_success = u"Вы успешно активировали свой акаунт"
secondary_regis_finish_error = u"Ссылка активации не активна"
secondary_main_forgot = u"Восстановление пароля"
reset_password_title = u"Сбросить пароль"
common_help_text = u"Внимание, при сбросе пароля устанавливается hold вывода средств на 36 часов"
forgot_sending_email_msg = u"На указаный электронный адрес было выслано письмо с новыми данными для авторизации"
withdraw_transfer = u"Отправить"
attention_be_aware = u"Будьте внимательны при заполнение реквизитов<br/> \n\
комиссия согласно условиям вашего банка"
withdraw_title_bank = u"Заявка на вывод банковским переводом"
withdraw_title_liqpay = u"Заявка на вывод через систему liqpay"
liqpay_attention_be_aware = u"Будьте внимательны при указание номера счета liqpay"
withdrawing_secondary_main_email_confirmation_title= u"Подтверждение по электронной почте"
withdrawing_sending_email_confirmation= u"Код для подтверждения вывода средств был направлен вам на электронный адрес"


withdrawing_error = u"Ошибка подтверждения"
withdraw_doesnot_existed = u"Вывод с таким кодом не найден, либо уже в работе, уточняйте вопрос  у службы поддержки"
withdraw_ok = u"Вывод подтвержден"
withdraw_msg_ok = u"Ваша заявка на вывод подтверждена, перевод будет осуществлен в ближайшее время"
p2p_transfer = u"Отправить"
p2p_attention_be_aware  = u"Будьте внимательны при заполении реквизитов,<br/>\n\
комиссия для вывода на Карту ПриватБанка 1&nbsp;%,<br/>\n\
Карта украинского банка 1.3&nbsp;%,<br/>\n\
Карта зарубежного банка 1,95 дол + 1&nbsp;%<br/>\n\
"
attention_be_aware_crypto = u"Будьте внимательны при заполении реквизитов,<br/>\n\
комиссия системы данной криптовалюты составляет %s&nbsp;<br/>\n\
"
pin_change_title = u"Смена PIN-кода"

crypto_fee = "0.0001"

MANAGERS = ADMINS

AUTH_USER_MODEL = 'auth.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',#  Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
     #   'NAME':  ROOT_PATH + 'crypton.db',                      # Or path to database file if using sqlite3.
		'NAME':'crypton_odessa',
		'USER':'odessa',
	    'PASSWORD':'odessa_pass',
	 	'HOST':'localhost',
		'PORT':'3307'
  },
   
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE ='Europe/Minsk'
FORCE_SCRIPT_NAME=''

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT':  30
    }
}

#SESSION_ENGINE='django.contrib.sessions.backends.cache'

# Language code for this installation. All choices can be found here:
# 
LANGUAGE_CODE = 'ru' #-RU'

LANGUAGE_COOKIE_NAME = "language"

LANGUAGES = (
    ('ru', 'Russian'),
    ('uk', 'Ukrainian'),
    ('en', 'English'),
)

LOCALE_PATHS = (
    ROOT_PATH + 'locale',
    # os.path.join(PROJECT_DIR, 'locale'),
)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

LOGIN_URL = '/helpdesk/login/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT =  ROOT_PATH + 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ROOT_PATH + 'img/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATIC_SERVER = "https://bitmoney.trade/" 
#"https://btc-trade.com.ua/"

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
}
TINYMCE_SPELLCHECKER = True
TINYMCE_JS_URL = 'https://bitmoney.trade/static/js/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True


# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/admin_media/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7&amp;1y&amp;$26-j3m6e=ico6x3j+klwwm)pi)vd^(_an0!(dzt9(r=w'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.CacheMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crypton.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crypton.wsgi.application'

TEMPLATE_DIRS = (
   ROOT_PATH + "tmpl",
   ROOT_PATH + "tmpl/admin/main",
   ROOT_PATH + "tmpl/admin/main/includes/user",
   ROOT_PATH + "tmpl/admin/main/auth",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     #'admin_tools',
    #'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard', 	
     'django.contrib.admin',
     #'django.contrib.markup', # Required for helpdesk text display
     'main',
    #'debug_toolbar',
     'captcha',
 #    'helpdesk',
    # Uncomment the next line to enable admin documentation:
     'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
if not DEBUG: 
   LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
  }
else:


  LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
       'require_debug_false': {
           '()': 'django.utils.log.RequireDebugFalse'
       }
     },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'

        },
    },
    'handlers': {
       'mail_admins': {
          'level': 'ERROR',
           'class': 'django.utils.log.AdminEmailHandler'
       },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': ROOT_PATH + 'crypton.log',
         },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            "formatter": "simple"
        },
        'django.request': {
            'handlers': ['file','console'],
            'level': 'DEBUG',
            'propagate': True,
            "formatter": "simple"

        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'crypton.main.api': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            "formatter": "simple"

        },
    }
        
  }

