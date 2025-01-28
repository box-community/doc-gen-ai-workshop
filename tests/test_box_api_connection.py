from src.client import AppConfig
from dotenv import load_dotenv
import os
load_dotenv()


    

def test_box_app_config_configuration():
    """ Should return a valid CCGConfig object from the environment variables """
    ap = AppConfig()
    assert ap.conf.client_id == os.getenv("BOX_CLIENT_ID")
    assert ap.conf.client_secret == os.getenv("BOX_CLIENT_SECRET")
    assert ap.conf.enterprise_id == os.getenv("BOX_ENTERPRISE_ID")
    assert ap.conf.user_id == os.getenv("BOX_USER_ID")
    
def test_box_app_config_auth():
    """Should return a valid BoxCCGAuth object from the environment variables"""
    ap = AppConfig()
    assert ap.auth.subject_type =="user"
    assert ap.auth.subject_id==os.getenv("BOX_USER_ID")
    assert ap.auth.retrieve_token() is not None

def test_box_app_config_client():
    """Should return a BocClient"""
    ap = AppConfig()
    client = ap.get_box_client()
    me = client.users.get_user_me()
    assert me.id == os.getenv("BOX_USER_ID")