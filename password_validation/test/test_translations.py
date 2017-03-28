# coding=utf-8
"""This module is backported from Django.

Copied from tests/auth_tests/test_validators.py at commit
9851e54121b3eebd3a7a29de3ed874d82554396b

The only change is to replace `django.contrib.auth.password_validation` with
`password_validation` throughout.

"""
from __future__ import unicode_literals

import os

from django.contrib.auth.models import User
from django.utils import translation

from password_validation import (
    CommonPasswordValidator, MinimumLengthValidator, NumericPasswordValidator,
    UserAttributeSimilarityValidator, get_default_password_validators,
    get_password_validators, password_changed,
    password_validators_help_text_html, password_validators_help_texts,
    validate_password,
)
from django.core.exceptions import ValidationError
from django.test import TestCase, override_settings
from django.utils._os import upath


class TranslationTest(TestCase):
    def test_ru_translation(self):
        translation.activate('ru')
        try:
            MinimumLengthValidator().validate('test')
        except ValidationError as e:
            self.assertEqual(e.message,
                "Введённый пароль слишком короткий. Он должен содержать как минимум %(min_length)d символ.")
