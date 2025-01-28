from box_sdk_gen import (
    BoxClient,
    BoxCCGAuth,
    CCGConfig,
    FileWithInMemoryCacheTokenStorage,
)
from dotenv import load_dotenv
import os

load_dotenv()


class AppConfig:
    conf: CCGConfig
    auth: BoxCCGAuth
    workshop_parent_folder_id: str = "0"

    def __init__(self):
        self.conf = CCGConfig(
            client_id=os.getenv("BOX_CLIENT_ID"),
            client_secret=os.getenv("BOX_CLIENT_SECRET"),
            enterprise_id=os.getenv("BOX_ENTERPRISE_ID"),
            user_id=os.getenv("BOX_USER_ID"),
            token_storage=FileWithInMemoryCacheTokenStorage(
                filename=".box_token_storage"
            ),
        )

        self.auth = BoxCCGAuth(self.conf)

        self.workshop_parent_folder_id = os.getenv("BOX_WORKSHOP_PARENT_FOLDER_ID")

    def get_box_client(self) -> BoxClient:
        return BoxClient(self.auth)
