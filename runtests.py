#!/usr/bin/env python
# This script exists so this dir is on sys.path when running pytest in tox.
import pytest
import os
import sys

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'password_validation.test.settings')

sys.exit(pytest.main())
