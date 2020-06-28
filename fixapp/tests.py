#!/usr/bin/env python3
from __future__ import annotations

from django.apps import apps
from django.test import TestCase

from .apps import FixappConfig


class TestsFixappConfig(TestCase):
    def test_app(self: TestsFixappConfig) -> None:
        assert "fixapp" == FixappConfig.name
        assert "fixapp" == apps.get_app_config("fixapp").name
