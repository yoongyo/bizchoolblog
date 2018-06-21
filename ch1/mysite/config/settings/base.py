import os
import uuid
from datetime import datetime
import json
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


BASE1_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

# .config_secret 폴더 및 하위 파일 경로
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['secret_key']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django_summernote',
    'accounts',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(ROOT_DIR, 'mysite', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'mysite.wsgi.application'

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


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# 기본 로그인 페이지 URL을 지정
# login_required 장식자 등에 의해서 사용
LOGIN_URL = '/blog/login/'


# 로그인 완료 후에 next 인자가 지정되면 해당 URL로 페이지 이동
# next 인자가 없으면 본 URL로 이동
LOGIN_REDIRECT_URL = '/blog/new/'

# 로그아웃 완료 후에
# -next_page 인자가 지정되면 next_page URL로 페이지 이동
# -next_page 인자가 없으면 LOGOUT_REDIRECT_URL이 지정되었을 경우 해당 URL로 이동
# -next_page 인자가 None일 경우 redirect를 수행하지 않고
# 'registraion/logged_out.html' 템플릿을 렌더링
LOGOUT_REDIRECT_URL = None

# 인증에 사용할 커스텀 User 모델 지정, '앱이름.모델명'
AUTH_USER_MODEL = 'auth.User'


def uploaded_filepath(instance, filename):
    """
    Returns default filepath for uploaded files.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join('django-summernote', today, filename)


def get_attachment_model():
    """
    Returns the Attachment model that is active in this project.
    """
    try:
        from blog.models import AbstractAttachment
        klass = django_apps.get_model(summernote_config["attachment_model"])
        if not issubclass(klass, AbstractAttachment):
            raise ImproperlyConfigured(
                "SUMMERNOTE_CONFIG['attachment_model'] refers to model '%s' that is not "
                "inherited from 'django_summernote.models.AbstractAttachment'" % summernote_config["attachment_model"]
            )
        return klass
    except ValueError:
        raise ImproperlyConfigured("SUMMERNOTE_CONFIG['attachment_model'] must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "SUMMERNOTE_CONFIG['attachment_model'] refers to model '%s' that has not been installed" % summernote_config["attachment_model"]
        )


LANG_TO_LOCALE = {
    'ar': 'ar-AR',
    'bg': 'bg-BG',
    'ca': 'ca-ES',
    'cs': 'cs-CZ',
    'da': 'da-DK',
    'de': 'de-DE',
    'el': 'el-GR',
    'es': 'es-ES',
    'fa': 'fa-IR',
    'fi': 'fi-FI',
    'fr': 'fr-FR',
    'gl': 'gl-ES',
    'he': 'he-IL',
    'hr': 'hr-HR',
    'hu': 'hu-HU',
    'id': 'id-ID',
    'it': 'it-IT',
    'ja': 'ja-JP',
    'ko': 'ko-KR',
    'lt': 'lt-LT',
    'mn': 'mn-MN',
    'nb': 'nb-NO',
    'nl': 'nl-NL',
    'pl': 'pl-PL',
    'pt': 'pt-BR',
    'ro': 'ro-RO',
    'ru': 'ru-RU',
    'sk': 'sk-SK',
    'sl': 'sl-SI',
    'sr': 'sr-RS',
    'sv': 'sv-SE',
    'ta': 'ta-IN',
    'th': 'th-TH',
    'tr': 'tr-TR',
    'uk': 'uk-UA',
    'vi': 'vi-VN',
    'zh': 'zh-CN',
}

SETTINGS_USER = getattr(settings, 'SUMMERNOTE_CONFIG', {})
SETTINGS_DEFAULT = {
    # Using SummernoteWidget(iframe widget) for admin pages by default
    'iframe': True,

    # These strings will be assumed as empty.
    'empty': ('<p><br/></p>', '<p><br></p>'),

    # Language-to-locale conversion table
    'lang_matches': LANG_TO_LOCALE,

    # Attachment settings
    'disable_attachment': False,
    'attachment_upload_to': uploaded_filepath,
    'attachment_storage_class': None,
    'attachment_filesize_limit': 1024 * 1024,
    'attachment_require_authentication': False,
    'attachment_model': 'django_summernote.Attachment',

    # Shortcut name for jQuery
    'jquery': '$',

    # Base media files only for SummernoteWidget
    'base_css': (
        '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
    ),
    'base_js': (
        '//code.jquery.com/jquery-3.2.1.min.js',
        '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js',
    ),

    # Media files for CodeMirror
    'codemirror_css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/codemirror.min.css',
    ),
    'codemirror_js': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/codemirror.min.js',
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/mode/xml/xml.min.js',
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/mode/htmlmixed/htmlmixed.min.js',
    ),

    # Media files for all Summernote widgets
    'default_css': (
        'summernote/summernote.css',
        'summernote/django_summernote.css',
    ),
    'default_js': (
        'summernote/jquery.ui.widget.js',
        'summernote/jquery.iframe-transport.js',
        'summernote/jquery.fileupload.js',
        'summernote/summernote.min.js',
        'summernote/ResizeSensor.js',
    ),

    # Additional media files only for SummernoteWidget
    'css': (),
    'js': (),

    # Additional media files only for SummernoteInplacewidget
    'css_for_inplace': (),
    'js_for_inplace': (),

    # For lazy loading (inplace widget only)
    'lazy': False,

    # Summernote settings
    'summernote': {
        'width': 720,
        'height': 480,
        'lang': None,
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'superscript', 'subscript',
                      'strikethrough', 'clear']],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video', 'hr']],
            ['view', ['fullscreen', 'codeview']],
            ['help', ['help']],
        ],
    }
}

summernote_config = SETTINGS_DEFAULT.copy()
summernote_config.update(SETTINGS_USER)



def _copy_old_configs(config, user, default):
    """
    NOTE: Will be deprecated from 0.9
    Copying old-style settings for backword-compatibility
    """
    DEPRECATED_SUMMERNOTE_CONFIGS = (
        'width',
        'height',
        'lang',
        'toolbar',
    )
    for key in DEPRECATED_SUMMERNOTE_CONFIGS:
        if user.get(key):
            config['summernote'][key] = user.get(key)
        if not config['summernote'].get(key):
            config['summernote'][key] = default['summernote'].get(key)


_copy_old_configs(summernote_config, SETTINGS_USER, SETTINGS_DEFAULT)
