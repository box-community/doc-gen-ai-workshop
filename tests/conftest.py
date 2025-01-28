import pytest
from src.client import AppConfig
from box_sdk_gen import BoxClient


@pytest.fixture
def app_config()->AppConfig:
    return AppConfig()

@pytest.fixture
def box_client()->BoxClient:
    return AppConfig().get_box_client()
