# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/v/vdubanbu/vdubanbu.beget.tech/moloshop')
sys.path.insert(1, '/home/v/vdubanbu/vdubanbu.beget.tech/venv_moloshop/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'moloshop.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()