import pytest
from box_sdk_gen import BoxClient

from src.client import AppConfig


@pytest.fixture
def app_config() -> AppConfig:
    return AppConfig()


@pytest.fixture
def box_client() -> BoxClient:
    return AppConfig().get_box_client()
