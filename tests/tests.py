#!/usr/bin/env python3
from __future__ import annotations


class TestApp:
    def test_one(self: TestApp) -> None:
        x: str = "this"
        assert "h" in x
