import os
from django.core.wsgi import get_wsgi_application


if os.environ.get('DEBUG') or os.environ.get('heroku_config'):
    os.environ["DJANGO_SETTINGS_MODULE"] = 'RobotixWeb.settings'
else:
    os.environ["DJANGO_SETTINGS_MODULE"] = 'RobotixWeb.production'

application = get_wsgi_application()
