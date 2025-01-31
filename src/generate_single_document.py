import random

from box_sdk_gen import BoxClient, File, Folder, Items

from api import MergeData, get_doc_gen_script_data_full
from client import AppConfig


def get_random_movie_script(client: BoxClient, folder_id) -> File:
    """
    Get a random movie script from a folder.
    """
    items = client.folders.get_folder_items(folder_id, limit=30)
    files = [item for item in items.entries if item.type == "file"]

    return random.choice(files)


def main() -> None:
    """
    Main function to generate documents
    """
    # Get a box client
    ap = AppConfig()
    client = ap.get_box_client()

    # Check Box API connection
    user = client.users.get_user_me()
    print("\n\n-- Box API --\n")
    print(f"Connected to Box API as {user.name}")

    # Get a random file from the scripts folder
    box_movie_script = get_random_movie_script(client, ap.scripts_folder_id)

    # Hitchhiker's-Guide-to-the-Galaxy-The.pdf [1763001740428]
    # box_movie_script = client.files.get_file_by_id("1763001740428")

    # ID4.pdf [1763007947392]
    # box_movie_script = client.files.get_file_by_id("1763007947392")

    # Interstellar.pdf [1763015687737]
    # box_movie_script = client.files.get_file_by_id("1763015687737")

    # Prometheus.pdf [1763001446271]
    # box_movie_script = client.files.get_file_by_id("1763001446271")

    # Strange-Days.pdf [1763005303100]
    # box_movie_script = client.files.get_file_by_id("1763005303100")

    # Get merge data for this document
    print(f"Getting merge data for {box_movie_script.name} [{box_movie_script.id}]")
    merge_data: MergeData = get_doc_gen_script_data_full(client, box_movie_script)

    # for reference let's write this data to a json file.
    with open(f"{box_movie_script.name}_{box_movie_script.id}.json", "w") as f:
        f.write(merge_data.to_json(indent=4))
    print(f"Merge data written to {box_movie_script.name}.json")


if __name__ == "__main__":
    main()
