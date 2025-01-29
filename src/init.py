import os

from tqdm import tqdm

from api import create_folder, upload_file
from client import AppConfig


def main():
    ap = AppConfig()

    client = ap.get_box_client()

    # Create box workshop folder structure
    workshop_parent_folder = client.folders.get_folder_by_id(
        ap.workshop_parent_folder_id
    )
    print(f"Using parent folder: {workshop_parent_folder.name}")

    base_folder = create_folder(
        client, "Workshop (Doc Gen + AI)", workshop_parent_folder
    )
    print(f"Created folder: {base_folder.name}")

    scripts_folder = create_folder(client, "Scripts", base_folder)
    print(f"Created folder: {scripts_folder.name}")

    template_folder = create_folder(client, "Templates", base_folder)
    print(f"Created folder: {template_folder.name}")

    # upload template folder to box
    local_template = "sample_files/template/MovieScriptSummaryTemplate.docx"

    box_template = upload_file(
        client, local_template, template_folder, ignore_if_exists=False
    )
    print(f"Uploaded template: {box_template.name}")

    # update .env file with the new folder ids
    ap.set_workshop_folder_ids(
        base_folder.id, scripts_folder.id, template_folder.id, box_template.id
    )
    ap.write_env_file()
    ap.reload_dotenv()

    # upload scripts folder to box
    local_files = [
        "sample_files/scripts/" + f for f in os.listdir("sample_files/scripts")
    ]
    for local_file in tqdm(local_files, desc="Uploading scripts"):
        upload_file(client, local_file, scripts_folder)
        # print(f"Uploaded file: {box_file.name}")


if __name__ == "__main__":
    main()
