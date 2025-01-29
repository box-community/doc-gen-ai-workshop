import json

from box_sdk_gen import BoxClient, File

from src.api import (
    MergeData,
    get_doc_gen_character_list,
    get_doc_gen_directors,
    get_doc_gen_locations,
    get_doc_gen_producers,
    get_doc_gen_props,
    get_doc_gen_script_data,
    get_doc_gen_script_data_full,
    get_doc_gen_script_summary,
    get_doc_gen_writer,
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
    # print(merge_data.to_json())


def test_api_doc_gen_load_locations(box_client: BoxClient, test_sample_file: File):
    """Test the location list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_locations(box_client, test_sample_file)
    assert len(merge_data.locations) > 0
    # print(merge_data.to_json())


def test_api_doc_gen_load_props(box_client: BoxClient, test_sample_file: File):
    """Test the prop list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_props(box_client, test_sample_file)
    assert len(merge_data.props) > 0
    # print(merge_data.to_json())


def test_api_doc_gen_load_directors(box_client: BoxClient, test_sample_file: File):
    """Test the director list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_directors(box_client, test_sample_file)
    assert len(merge_data.directors) > 0
    # print(merge_data.to_json())


def test_api_doc_gen_load_producers(box_client: BoxClient, test_sample_file: File):
    """Test the producer list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_producers(box_client, test_sample_file)
    assert len(merge_data.producers) > 0
    # print(merge_data.to_json())


def test_api_doc_gen_load_writer(box_client: BoxClient, test_sample_file: File):
    """Test the writer list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_writer(box_client, test_sample_file)
    print(merge_data.to_json())

    assert len(merge_data.screen_writer) > 0
    assert merge_data.screen_writer.get("name") == "James Cameron"
    assert len(merge_data.screen_writer.other_scripts) > 0
    assert len(merge_data.screen_writer.accomplishments) > 0
    assert len(merge_data.screen_writer.other_scripts) > 0
    assert len(merge_data.screen_writer.produced_movies) > 0
    assert len(merge_data.screen_writer.produced_movies) > 0
    assert len(merge_data.screen_writer.produced_movies[0].title) > 0
    assert len(merge_data.screen_writer.produced_movies[0].gross_revenue) > 0


def test_api_doc_gen_load_script_data_full(
    box_client: BoxClient, test_sample_file: File
):
    """Test the full script data API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_script_data_full(box_client, test_sample_file)
    print(merge_data.to_json())

    assert merge_data.title == "Aliens"
    assert merge_data.author == "James Cameron"
    assert merge_data.genre == "Action Horror Sci-Fi Thriller"
    assert merge_data.date_written == "May 28, 1985"
    assert len(merge_data.summary) > 0
    assert len(merge_data.character_list) > 0
    assert len(merge_data.locations) > 0
    assert len(merge_data.props) > 0
    assert len(merge_data.directors) > 0
    assert len(merge_data.producers) > 0
    assert len(merge_data.screen_writer) > 0
    assert merge_data.screen_writer.name == "James Cameron"
    assert len(merge_data.screen_writer.other_scripts) > 0
    assert len(merge_data.screen_writer.accomplishments) > 0
    assert len(merge_data.screen_writer.other_scripts) > 0
    assert len(merge_data.screen_writer.produced_movies) > 0
    assert len(merge_data.screen_writer.produced_movies) > 0
    assert len(merge_data.screen_writer.produced_movies[0].title) > 0
    assert len(merge_data.screen_writer.produced_movies[0].gross_revenue) > 0
