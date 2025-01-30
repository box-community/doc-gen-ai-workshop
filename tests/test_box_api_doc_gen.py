from box_sdk_gen import BoxClient, File

from src.api import (
    MergeData,
    get_doc_gen_character_list,
    get_doc_gen_directors,
    get_doc_gen_producers,
    get_doc_gen_script_data,
    get_doc_gen_script_data_full,
    get_doc_gen_smart_load,
    get_doc_gen_writer,
)


def test_api_doc_gen_load_merge_data(box_client: BoxClient, test_sample_file: File):
    """Test the script data API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_script_data(box_client, test_sample_file)
    # print(merge_data.to_json())

    assert merge_data.script.title == "Aliens"
    assert merge_data.script.author == "James Cameron"
    assert merge_data.script.genre == "Action Horror Sci-Fi Thriller"
    assert merge_data.script.date_written == "May 28, 1985"
    # summary
    assert len(merge_data.script.plot_summary) > 0
    # locations
    assert len(merge_data.script.locations) > 0
    assert merge_data.script.locations[0].name != ""
    # props
    assert len(merge_data.script.props) > 0
    assert merge_data.script.props[0].name != ""


def test_api_doc_gen_load_character_list(box_client: BoxClient, test_sample_file: File):
    """Test the character list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_character_list(box_client, test_sample_file)
    # print(merge_data.to_json())
    assert len(merge_data.character_list) > 0
    assert merge_data.character_list[0].name != ""
    assert len(merge_data.character_list[0].suggested_actors) > 0
    assert merge_data.character_list[0].suggested_actors[0] != ""


def test_api_doc_gen_smart_load(box_client: BoxClient, test_sample_file: File):
    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_smart_load(box_client, test_sample_file)
    # print(merge_data.to_json())

    assert len(merge_data.directors) > 0
    assert len(merge_data.producers) > 0
    assert merge_data.screen_writer.name == "James Cameron"
    assert len(merge_data.screen_writer.other_scripts) > 0
    assert len(merge_data.screen_writer.accomplishments) > 0
    assert len(merge_data.screen_writer.produced_movies) > 0
    assert len(merge_data.screen_writer.companies_worked_with) > 0


# TODO: Load Producers and Directors and Writers in the same request
def test_api_doc_gen_load_directors(box_client: BoxClient, test_sample_file: File):
    """Test the director list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_directors(box_client, test_sample_file)
    # print(merge_data.to_json())
    assert len(merge_data.directors) > 0
    assert merge_data.directors[0].name != ""


def test_api_doc_gen_load_producers(box_client: BoxClient, test_sample_file: File):
    """Test the producer list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_producers(box_client, test_sample_file)
    # print(merge_data.to_json())

    assert len(merge_data.producers) > 0
    assert merge_data.producers[0].name != ""


def test_api_doc_gen_load_writer(box_client: BoxClient, test_sample_file: File):
    """Test the writer list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_writer(box_client, test_sample_file)
    # print(merge_data.to_json())

    assert merge_data.screen_writer.name == "James Cameron"
    assert merge_data.screen_writer.other_scripts is not None
    assert merge_data.screen_writer.accomplishments is not None
    assert merge_data.screen_writer.other_scripts is not None
    assert merge_data.screen_writer.produced_movies is not None
    assert len(merge_data.screen_writer.produced_movies[0].title) > 0
    assert len(merge_data.screen_writer.produced_movies[0].gross_revenue) > 0


def test_api_doc_gen_load_script_data_full(
    box_client: BoxClient, test_sample_file: File
):
    """Test the full script data API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: MergeData = get_doc_gen_script_data_full(box_client, test_sample_file)
    print(merge_data.to_json())

    assert merge_data.script.title == "Aliens"
    assert merge_data.script.author == "James Cameron"
    assert merge_data.script.genre == "Action Horror Sci-Fi Thriller"
    assert merge_data.script.date_written == "May 28, 1985"
    assert len(merge_data.script.plot_summary) > 0
    assert len(merge_data.script.locations) > 0
    assert len(merge_data.script.props) > 0

    assert len(merge_data.character_list) > 0

    assert len(merge_data.directors) > 0
    assert len(merge_data.producers) > 0

    assert merge_data.screen_writer.name == "James Cameron"
    assert merge_data.screen_writer.other_scripts is not None
    assert merge_data.screen_writer.accomplishments is not None
    assert merge_data.screen_writer.other_scripts is not None
    assert merge_data.screen_writer.produced_movies is not None
    assert len(merge_data.screen_writer.produced_movies[0].title) > 0
    assert len(merge_data.screen_writer.produced_movies[0].gross_revenue) > 0
