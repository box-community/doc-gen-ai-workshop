import pytest
from box_sdk_gen import BoxClient

from src.api import create_folder, upload_file
from src.client import AppConfig


@pytest.fixture(scope="module")
def app_config() -> AppConfig:
    return AppConfig()


@pytest.fixture(scope="module")
def box_client() -> BoxClient:
    return AppConfig().get_box_client()


@pytest.fixture(scope="module")
def test_sample_file(box_client: BoxClient):
    # Create a folder
    root_folder = box_client.folders.get_folder_by_id("0")
    folder_name = "Doc Gen+AI Workshop tests folder"
    box_test_folder = create_folder(box_client, folder_name, root_folder)

    # Upload local sample data
    local_file_path = "tests/data/Aliens - by James Cameron.pdf"
    box_file = upload_file(box_client, local_file_path, box_test_folder)

    yield box_file

    # remove folder
    box_client.folders.delete_folder_by_id(box_test_folder.id, recursive=True)
