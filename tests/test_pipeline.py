"""Tests."""
import pytest
from src.config import Config


def test_config_defaults():
    config = Config()
    assert config.model == "mimo-v2.5"
    assert config.temperature == 0.3
    assert config.max_tokens == 4096


def test_config_from_env(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
    monkeypatch.setenv("DEEPSEEK_MODEL", "mimo-v2.5-pro")
    config = Config()
    assert config.api_key == "test-key"
    assert config.model == "mimo-v2.5-pro"
