import os

from dotenv import load_dotenv

from src.client import AppConfig

load_dotenv()


def test_box_app_config_configuration():
    """Should return a valid CCGConfig object from the environment variables"""
    ap = AppConfig()
    assert ap.conf.client_id == os.getenv("BOX_CLIENT_ID")
    assert ap.conf.client_secret == os.getenv("BOX_CLIENT_SECRET")
    assert ap.conf.enterprise_id == os.getenv("BOX_ENTERPRISE_ID")
    assert ap.conf.user_id == os.getenv("BOX_USER_ID")


def test_box_app_config_auth():
    """Should return a valid BoxCCGAuth object from the environment variables"""
    ap = AppConfig()
    assert ap.auth.subject_type == "user"
    assert ap.auth.subject_id == os.getenv("BOX_USER_ID")
    assert ap.auth.retrieve_token() is not None


def test_box_app_config_client():
    """Should return a BocClient"""
    ap = AppConfig()
    client = ap.get_box_client()
    me = client.users.get_user_me()
    assert me.id == os.getenv("BOX_USER_ID")


def test_box_app_config_write_env_file():
    """Should write the .env file with the configurations from the AppConfig object"""
    ap = AppConfig()

    assert ap.workshop_parent_folder_id == os.getenv(
        "BOX_WORKSHOP_PARENT_FOLDER_ID", ""
    )
    assert ap.workshop_folder_id == os.getenv("BOX_WORKSHOP_FOLDER_ID", "")
    assert ap.scripts_folder_id == os.getenv("BOX_SCRIPTS_FOLDER_ID", "")
    assert ap.templates_folder_id == os.getenv("BOX_TEMPLATES_FOLDER_ID", "")

    assert ap.conf.client_id == os.getenv("BOX_CLIENT_ID")
    assert ap.conf.client_secret == os.getenv("BOX_CLIENT_SECRET")
    assert ap.conf.enterprise_id == os.getenv("BOX_ENTERPRISE_ID")
    assert ap.conf.user_id == os.getenv("BOX_USER_ID")

    ap.set_workshop_folder_ids(
        workshop_folder_id="1",
        scripts_folder_id="2",
        templates_folder_id="3",
        doc_gen_template_file_id="4",
        merge_folder_id="5",
    )
    ap.write_env_file()
    ap.reload_dotenv()

    assert ap.workshop_parent_folder_id == os.getenv(
        "BOX_WORKSHOP_PARENT_FOLDER_ID", ""
    )
    assert ap.workshop_folder_id == "1"
    assert ap.scripts_folder_id == "2"
    assert ap.templates_folder_id == "3"
    assert ap.doc_gen_template_file_id == "4"
    assert ap.merge_folder_id == "5"

    assert ap.conf.client_id == os.getenv("BOX_CLIENT_ID")
    assert ap.conf.client_secret == os.getenv("BOX_CLIENT_SECRET")
    assert ap.conf.enterprise_id == os.getenv("BOX_ENTERPRISE_ID")
    assert ap.conf.user_id == os.getenv("BOX_USER_ID")

    ap.set_workshop_folder_ids(
        workshop_folder_id="",
        scripts_folder_id="",
        templates_folder_id="",
        doc_gen_template_file_id="",
        merge_folder_id="",
    )
    ap.write_env_file()
    ap.reload_dotenv()

    assert ap.workshop_parent_folder_id == os.getenv(
        "BOX_WORKSHOP_PARENT_FOLDER_ID", ""
    )
    assert ap.workshop_folder_id == ""
    assert ap.scripts_folder_id == ""
    assert ap.templates_folder_id == ""

    assert ap.conf.client_id == os.getenv("BOX_CLIENT_ID")
    assert ap.conf.client_secret == os.getenv("BOX_CLIENT_SECRET")
    assert ap.conf.enterprise_id == os.getenv("BOX_ENTERPRISE_ID")
    assert ap.conf.user_id == os.getenv("BOX_USER_ID")
