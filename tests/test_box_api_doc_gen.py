from box_sdk_gen import BoxClient, File

from src.api import (
    Script,
    get_doc_gen_character_list,
    get_doc_gen_directors,
    get_doc_gen_producers,
    get_doc_gen_script_data,
    get_doc_gen_script_data_full,
    get_doc_gen_smart_load,
)


def test_api_doc_gen_load_merge_data(box_client: BoxClient, test_sample_file: File):
    """Test the script data API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: Script = get_doc_gen_script_data(box_client, test_sample_file)
    # print(merge_data.to_json())

    assert merge_data.title == "Aliens"
    assert merge_data.author == "James Cameron"
    assert merge_data.genre == "Action Horror Sci-Fi Thriller"
    assert merge_data.date_written == "May 28, 1985"


def test_api_doc_gen_load_character_list(box_client: BoxClient, test_sample_file: File):
    """Test the character list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: Script = get_doc_gen_character_list(box_client, test_sample_file)
    # print(merge_data.to_json())
    assert len(merge_data.character_list) > 0
    assert merge_data.character_list[0].name != ""
    assert len(merge_data.character_list[0].suggested_actors) > 0
    assert merge_data.character_list[0].suggested_actors[0] != ""


def test_api_doc_gen_smart_load(box_client: BoxClient, test_sample_file: File):
    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: Script = get_doc_gen_smart_load(box_client, test_sample_file)
    # print(merge_data.to_json())

    # assert merge_data.title == "Aliens"
    # assert merge_data.author == "James Cameron"
    # assert merge_data.genre == "Action Horror Sci-Fi Thriller"
    # assert merge_data.date_written == "May 28, 1985"
    # assert len(merge_data.plot_summary) > 0

    assert len(merge_data.locations) > 0
    assert len(merge_data.props) > 0

    # assert len(merge_data.character_list) > 0
    # assert merge_data.character_list[0].name != ""
    # assert len(merge_data.character_list[0].suggested_actors) > 0

    assert len(merge_data.directors) > 0
    assert len(merge_data.producers) > 0

    assert merge_data.accomplishments is not None
    assert merge_data.other_scripts is not None

    assert merge_data.produced_movies is not None
    assert len(merge_data.produced_movies[0].title) > 0
    assert len(merge_data.produced_movies[0].gross_revenue) > 0

    assert len(merge_data.companies_worked_with) > 0
    assert merge_data.companies_worked_with[0].description != ""


def test_api_doc_gen_load_directors(box_client: BoxClient, test_sample_file: File):
    """Test the director list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: Script = get_doc_gen_directors(box_client, test_sample_file)
    # print(merge_data.to_json())
    assert len(merge_data.directors) > 0
    assert merge_data.directors[0].name != ""


def test_api_doc_gen_load_producers(box_client: BoxClient, test_sample_file: File):
    """Test the producer list API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: Script = get_doc_gen_producers(box_client, test_sample_file)
    # print(merge_data.to_json())

    assert len(merge_data.producers) > 0
    assert merge_data.producers[0].name != ""


def test_api_doc_gen_load_script_data_full(
    box_client: BoxClient, test_sample_file: File
):
    """Test the full script data API doc generation."""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    merge_data: Script = get_doc_gen_script_data_full(box_client, test_sample_file)
    print(merge_data.to_json())

    assert merge_data.title == "Aliens"
    assert merge_data.author == "James Cameron"
    assert merge_data.genre == "Action Horror Sci-Fi Thriller"
    assert merge_data.date_written == "May 28, 1985"
    assert len(merge_data.plot_summary) > 0
    assert len(merge_data.locations) > 0
    assert len(merge_data.props) > 0

    assert len(merge_data.character_list) > 0

    assert len(merge_data.directors) > 0
    assert len(merge_data.producers) > 0

    assert merge_data.accomplishments is not None
    assert merge_data.other_scripts is not None
    assert merge_data.produced_movies is not None
    assert len(merge_data.produced_movies[0].title) > 0
    assert len(merge_data.produced_movies[0].gross_revenue) > 0
    assert len(merge_data.companies_worked_with) > 0
