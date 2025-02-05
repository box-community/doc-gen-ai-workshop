import os
import random

from box_sdk_gen import BoxClient, File

from api import MergeData, get_doc_gen_script_data_full
from client import AppConfig


def get_random_movie_script(client: BoxClient, folder_id) -> File:
    """
    Get a random movie script from a folder.
    """
    items = client.folders.get_folder_items(folder_id, limit=30)
    box_files = [item for item in items.entries if item.type == "file"]

    json_files = [f for f in os.listdir("output") if f.endswith(".json")]
    file_ids = [int(f.split("_")[1].split(".")[0]) for f in json_files]

    box_files = [f for f in box_files if f.id not in file_ids]

    return random.choice(box_files)


def main() -> None:
    """
    Main function to generate documents
    """
    # Get a box client
    ap = AppConfig()
    client = ap.get_box_client()

    # Check Box API connection
    user = client.users.get_user_me()
    print("\n\n-- Box API --")
    print(f"Connected to Box API as {user.name}")

    # Get a random file from the scripts folder
    box_movie_script = get_random_movie_script(client, ap.scripts_folder_id)

    # Get merge data for this document
    print(f"Getting merge data for {box_movie_script.name} [{box_movie_script.id}]")
    merge_data: MergeData = get_doc_gen_script_data_full(client, box_movie_script)

    # for reference let's write this data to a json file.
    with open(f"output/{box_movie_script.name}_{box_movie_script.id}.json", "w") as f:
        f.write(merge_data.to_json(indent=4))
    print(f"Merge data written to {box_movie_script.name}.json")


if __name__ == "__main__":
    main()
