import json
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum

from box_sdk_gen import BoxClient, File

from . import get_ai_character_list, get_ai_plot_summary, get_ai_script_data


@dataclass
@dataclass
class Character:
    name: str = ""
    description: str = ""
    suggested_actors: list[str] = None

    def to_dict(self):
        return self.__dict__.copy()

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


@dataclass
class MergeData:
    title: str = ""
    author: str = ""
    genre: str = ""
    date_written: str = ""
    summary: str = ""
    character_list: list[Character] = None

    def to_dict(self):
        return self.__dict__.copy()

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


def get_doc_gen_script_data(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get script data
    # {"Author": "James Cameron", "Genre": "Action Horror Sci-Fi Thriller", "Date written": "May 28, 1985"}
    script_data = get_ai_script_data(box_client, file)

    # Eliminate double spacing in answer
    script_data.answer = " ".join(script_data.answer.split())
    script_data_json = json.loads(script_data.answer)

    merge_data.title = script_data_json["Title"]
    merge_data.author = script_data_json["Author"]
    merge_data.genre = script_data_json["Genre"]
    merge_data.date_written = script_data_json["Date written"]

    return merge_data


def get_doc_gen_script_summary(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get script summary
    script_summary = get_ai_plot_summary(box_client, file)

    # Eliminate double spacing in answer
    script_summary.answer = " ".join(script_summary.answer.split())

    merge_data.summary = script_summary.answer

    return merge_data


def get_doc_gen_character_list(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get character list
    script_character_list = get_ai_character_list(box_client, file)

    # Eliminate double spacing in answer
    script_character_list.answer = " ".join(script_character_list.answer.split())
    # Eliminate ``` from answer
    script_character_list.answer = script_character_list.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_character_list.answer = script_character_list.answer.replace("json", "")

    xxx = json.loads(script_character_list.answer)

    merge_data.character_list = xxx.get("characters")

    return merge_data
