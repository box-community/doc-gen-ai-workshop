import logging

from box_sdk_gen import AiResponseFull, BoxClient, File

from src.api import (
    get_ai_character_list,
    get_ai_director_recommendations,
    get_ai_producer_recommendations,
    get_ai_script_data_extract,
)

logger = logging.getLogger(__name__)


def test_api_ai_character_list(box_client: BoxClient, test_sample_file: File):
    """Test AI character list of a Box file"""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    ai_response: AiResponseFull = get_ai_character_list(box_client, test_sample_file)

    assert ai_response.answer is not None


def test_api_ai_director_recommendations(box_client: BoxClient, test_sample_file: File):
    """Test AI location information of a Box file"""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    ai_response: AiResponseFull = get_ai_director_recommendations(
        box_client, test_sample_file
    )

    assert ai_response.answer is not None


def test_api_ai_producer_recommendations(box_client: BoxClient, test_sample_file: File):
    """Test AI location information of a Box file"""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    ai_response: AiResponseFull = get_ai_producer_recommendations(
        box_client, test_sample_file
    )

    assert ai_response.answer is not None


def test_api_ai_script_data(box_client: BoxClient, test_sample_file: File):
    """Test AI location information of a Box file"""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    ai_response: AiResponseFull = get_ai_script_data_extract(
        box_client, test_sample_file
    )

    assert ai_response.answer is not None
