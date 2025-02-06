import json
import os
import random

from box_sdk_gen import (
    CreateDocgenBatchV2025R0DestinationFolder,
    DocGenBatchBaseV2025R0,
    DocGenDocumentGenerationDataV2025R0,
    FileReferenceV2025R0,
)

from client import AppConfig


def get_random_movie_data() -> str:
    """
    Get a random movie script from the local output/*.json folder.
    """
    # read all the json files in the output folder
    json_files = [f for f in os.listdir("output") if f.endswith(".json")]
    json_file = random.choice(json_files)
    movie_data = json.load(open(f"output/{json_file}"))
    file_name = json_file.split(".")[0]
    return movie_data, file_name


def get_sample_movie_data() -> str:
    """
    Get a sample movie script from the local output/*.json folder.
    """
    # read Aliens - by James Cameron.pdf_1763008939159 in the output folder
    json_file = "Aliens - by James Cameron.pdf_1767602238773.json"

    movie_data = json.load(open(f"output/{json_file}"))
    file_name = json_file.split(".")[0]
    return movie_data, file_name


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

    # source_data, file_name = get_random_movie_data()
    source_data, file_name = get_sample_movie_data()

    movie_data = {}
    movie_data["script"] = source_data
    # print(f"\n\n{json.dumps(movie_data, indent=4)}\n\n")

    # Read tags from template file
    # tags: DocGenTagsV2025R0 = client.docgen_template.get_docgen_template_tags_v2025_r0(
    #     ap.doc_gen_template_file_id
    # )
    # print(f"\nTags: {tags.to_dict()}\n\n")

    print(f"Using movie data from {file_name}")

    file_reference = FileReferenceV2025R0(ap.doc_gen_template_file_id)
    destination_folder = CreateDocgenBatchV2025R0DestinationFolder(ap.merge_folder_id)
    document_data = DocGenDocumentGenerationDataV2025R0(file_name, movie_data)

    # Merger the files
    merge_batch: DocGenBatchBaseV2025R0 = client.docgen.create_docgen_batch_v2025_r0(
        file=file_reference,
        input_source="api",
        destination_folder=destination_folder,
        output_type="pdf",
        document_generation_data=[document_data],
    )
    print(f"Merge batch created: {merge_batch.id}")


if __name__ == "__main__":
    main()
