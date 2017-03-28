#!/usr/bin/env bash

cd password_validation
DJANGO_SETTINGS_MODULE='password_validation.test.settings' django-admin makemessages  -a --no-obsolete
# fix fuzzy strings
find locale -type f -exec sed -i 's/\#, fuzzy, python-format//g' {} +
DJANGO_SETTINGS_MODULE='password_validation.test.settings' django-admin compilemessages

