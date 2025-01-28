from client import AppConfig
from api import upload_file, create_folder
from tqdm import tqdm
import os
from box_sdk_gen import CreateFolderParent


def main():
    ap = AppConfig()

    client = ap.get_box_client()

    # Create box workshop folder structure
    workshop_parent_folder = client.folders.get_folder_by_id(
        ap.workshop_parent_folder_id
    )

    base_folder = create_folder(
        client, "Workshop (Doc Gen + AI)", workshop_parent_folder
    )
    print(f"Created folder: {base_folder.name}")

    scripts_folder = create_folder(client, "Scripts", base_folder)
    print(f"Created folder: {scripts_folder.name}")

    template_folder = create_folder(client, "Templates", base_folder)
    print(f"Created folder: {template_folder.name}")

    # update .env file with the new folder ids
    with open(".env", "a") as f:
        f.write(f"BOX_WORKSHOP_FOLDER_ID={base_folder.id}\n")
        f.write(f"BOX_SCRIPTS_FOLDER_ID={scripts_folder.id}\n")
        f.write(f"BOX_TEMPLATES_FOLDER_ID={template_folder.id}\n")

    # upload scripts folder to box
    local_files = [
        "sample_files/scripts/" + f for f in os.listdir("sample_files/scripts")
    ]
    for local_file in tqdm(local_files, desc="Uploading files"):
        box_file = upload_file(client, local_file, scripts_folder)
        # print(f"Uploaded file: {box_file.name}")

    # upload template folder to box
    local_files = [
        "sample_files/template/" + f for f in os.listdir("sample_files/template")
    ]
    for local_file in tqdm(local_files, desc="Uploading files"):
        box_file = upload_file(
            client, local_file, template_folder, ignore_if_exists=False
        )
        # print(f"Uploaded file: {box_file.name}")


if __name__ == "__main__":
    main()
