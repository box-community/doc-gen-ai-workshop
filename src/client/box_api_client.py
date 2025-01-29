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
    workshop_parent_folder_id: str = ""
    workshop_folder_id: str = ""
    scripts_folder_id: str = ""
    templates_folder_id: str = ""

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

        self.workshop_parent_folder_id = os.getenv("BOX_WORKSHOP_PARENT_FOLDER_ID", "")
        self.workshop_folder_id = os.getenv("BOX_WORKSHOP_FOLDER_ID", "")
        self.scripts_folder_id = os.getenv("BOX_SCRIPTS_FOLDER_ID", "")
        self.templates_folder_id = os.getenv("BOX_TEMPLATES_FOLDER_ID", "")

    def get_box_client(self) -> BoxClient:
        return BoxClient(self.auth)

    def write_env_file(self):
        with open(".env", "w") as f:
            f.write("# Connection parameters\n")
            f.write(f"BOX_CLIENT_ID = {self.conf.client_id}\n")
            f.write(f"BOX_CLIENT_SECRET = {self.conf.client_secret}\n")
            f.write("\n")
            f.write("# User parameters\n")
            f.write(f"BOX_ENTERPRISE_ID = {self.conf.enterprise_id}\n")
            f.write(f"BOX_USER_ID = {self.conf.user_id}\n")
            f.write("\n")
            f.write("# Workshop parent folder (Workshop folder will be created here)\n")
            f.write(
                f"BOX_WORKSHOP_PARENT_FOLDER_ID = {self.workshop_parent_folder_id}\n"
            )
            f.write("\n")
            f.write("# Workshop folder IDs\n")
            f.write(f"BOX_WORKSHOP_FOLDER_ID = {self.workshop_folder_id}\n")
            f.write(f"BOX_SCRIPTS_FOLDER_ID = {self.scripts_folder_id}\n")
            f.write(f"BOX_TEMPLATES_FOLDER_ID = {self.templates_folder_id}\n")

    def set_workshop_folder_ids(
        self, workshop_folder_id: str, scripts_folder_id: str, templates_folder_id: str
    ):
        self.workshop_folder_id = workshop_folder_id
        self.scripts_folder_id = scripts_folder_id
        self.templates_folder_id = templates_folder_id

    def reload_dotenv(self):
        for key, value in os.environ.items():
            if key.startswith("BOX_"):
                # print(f"Deleting {key}: {value} from os.environ")
                del os.environ[key]
        load_dotenv()
