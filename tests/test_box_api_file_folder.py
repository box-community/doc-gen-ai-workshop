from src.api import create_folder, upload_file
from src.client import AppConfig


def test_api_file_folder_create_folder(app_config: AppConfig):
    """Test creating a folder in Box"""

    client = app_config.get_box_client()

    box_parent_folder = client.folders.get_folder_by_id("0")

    box_folder = create_folder(client, "test_folder", box_parent_folder)

    assert box_folder.name == "test_folder"

    box_sub_folder = create_folder(client, "test_sub_folder", box_folder)
    assert box_sub_folder.name == "test_sub_folder"
    assert box_sub_folder.parent.id == box_folder.id

    # create the folder again
    box_folder_duplicate = create_folder(client, "test_folder", box_parent_folder)

    assert box_folder_duplicate.name == "test_folder"
    assert box_folder_duplicate.id == box_folder.id

    client.folders.delete_folder_by_id(box_folder.id, recursive=True)


def test_api_file_folder_upload_file(app_config: AppConfig):
    """Test uploading a file to Box"""

    client = app_config.get_box_client()

    local_file_path = "tests/data/test_upload.txt"
    box_parent_folder = client.folders.get_folder_by_id("0")

    box_file = upload_file(client, local_file_path, box_parent_folder)
    assert box_file.name == "test_upload.txt"

    box_file = upload_file(
        client, local_file_path, box_parent_folder, ignore_if_exists=True
    )
    assert box_file.name == "test_upload.txt"

    box_file = upload_file(
        client, local_file_path, box_parent_folder, ignore_if_exists=False
    )
    assert box_file.name == "test_upload.txt"

    client.files.delete_file_by_id(box_file.id)
