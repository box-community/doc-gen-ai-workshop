import json
import logging
from datetime import datetime
from pathlib import Path
from time import sleep

from tqdm import tqdm

from api import MergeData, get_doc_gen_script_data_full
from client import AppConfig


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

    items = client.folders.get_folder_items(ap.scripts_folder_id, limit=30)
    box_files = [item for item in items.entries if item.type == "file"]
    print(f"Found {len(box_files)} files in the folder")
    print("-------------------")

    output_folder = Path("output")
    output_folder.mkdir(parents=True, exist_ok=True)
    error_log_file = (
        output_folder / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_error_log.txt"
    )
    logging.basicConfig(
        filename=error_log_file,
        level=logging.ERROR,
    )
    with tqdm(total=len(box_files)) as progress_bar:
        for box_file in box_files:
            output_file = output_folder / f"{box_file.name}_{box_file.id}.json"

            # Skip file if we already have a json file in the output folder
            if output_file.exists():
                progress_bar.write(
                    f"Skipping {box_file.name} [{box_file.id}] as it already exists"
                )
                progress_bar.update(1)
                sleep(0.5)
                continue

            try:
                progress_bar.write(f"Processing {box_file.name} [{box_file.id}]")
                merge_data: MergeData = get_doc_gen_script_data_full(client, box_file)

                # Write this data to a json file
                with output_file.open("w") as f:
                    json.dump(merge_data.to_dict(), f, indent=4)
                progress_bar.update(1)

            except Exception as e:
                progress_bar.write(
                    f"\tError processing {box_file.name} [{box_file.id}]"
                )

                # Log the exception details on a separate log file using logger
                logging.error(f"Error processing {box_file.name} [{box_file.id}]")
                logging.error(e)
                logging.info("-")
                progress_bar.update(1)
                sleep(0.5)
                continue


if __name__ == "__main__":
    main()
