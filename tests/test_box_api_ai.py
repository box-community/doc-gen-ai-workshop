import logging

import pytest
from box_sdk_gen import AiResponseFull, BoxClient, File

from src.api import get_ai_character_list, get_ai_plot_summary

logger = logging.getLogger(__name__)


def test_api_ai_plot_summary(box_client: BoxClient, test_sample_file: File):
    """Test AI plot summary of a Box file"""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    ai_response: AiResponseFull = get_ai_plot_summary(box_client, test_sample_file)

    assert ai_response.answer is not None
    # print(ai_response.answer)


def test_api_ai_character_list(box_client: BoxClient, test_sample_file: File):
    """Test AI character list of a Box file"""

    assert test_sample_file.name == "Aliens - by James Cameron.pdf"

    ai_response: AiResponseFull = get_ai_character_list(box_client, test_sample_file)

    assert ai_response.answer is not None
    # print(ai_response.answer)
