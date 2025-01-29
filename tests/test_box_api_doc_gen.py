import json

from box_sdk_gen import BoxClient, File

from src.api import (
    MergeData,
    get_doc_gen_character_list,
    get_doc_gen_script_data,
    get_doc_gen_script_summary,
)


def test_api_doc_gen_load_merge_data(box_client: BoxClient, test_sample_file: File):
    """Test the script data API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_script_data(box_client, test_sample_file)
    assert merge_data.author == "James Cameron"
    assert merge_data.genre == "Action Horror Sci-Fi Thriller"
    assert merge_data.date_written == "May 28, 1985"
    # print(merge_data.to_json())


def test_api_doc_gen_load_script_summary(box_client: BoxClient, test_sample_file: File):
    """Test the script summary API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_script_summary(box_client, test_sample_file)
    assert len(merge_data.summary) > 0
    # print(merge_data.to_json())


def test_api_doc_gen_load_character_list(box_client: BoxClient, test_sample_file: File):
    """Test the character list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_character_list(box_client, test_sample_file)
    assert len(merge_data.character_list) > 0
    print(merge_data.to_json())
