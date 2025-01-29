import json
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum

from box_sdk_gen import BoxClient, File

from . import (
    get_ai_character_list,
    get_ai_director_recommendations,
    get_ai_location_information,
    get_ai_plot_summary,
    get_ai_producer_recommendations,
    get_ai_prop_list,
    get_ai_script_data,
)


@dataclass
class Producer:
    name: str = ""
    description: str = ""

    def to_dict(self):
        return self.__dict__.copy()

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


@dataclass
class Director:
    name: str = ""
    description: str = ""

    def to_dict(self):
        return self.__dict__.copy()

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


@dataclass
class Prop:
    name: str = ""
    description: str = ""

    def to_dict(self):
        return self.__dict__.copy()

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


@dataclass
class Location:
    name: str = ""
    description: str = ""

    def to_dict(self):
        return self.__dict__.copy()

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


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
    locations: list[Location] = None
    props: list[Prop] = None
    directors: list[Director] = None
    producers: list[Producer] = None

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
    json_answer = json.loads(script_character_list.answer)
    merge_data.character_list = json_answer.get("characters")

    return merge_data


def get_doc_gen_locations(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get character list
    script_locations = get_ai_location_information(box_client, file)

    # Eliminate double spacing in answer
    script_locations.answer = " ".join(script_locations.answer.split())
    # Eliminate ``` from answer
    script_locations.answer = script_locations.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_locations.answer = script_locations.answer.replace("json", "")
    json_answer = json.loads(script_locations.answer)
    merge_data.locations = json_answer.get("locations")

    return merge_data


def get_doc_gen_props(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get character list
    script_props = get_ai_prop_list(box_client, file)

    # Eliminate double spacing in answer
    script_props.answer = " ".join(script_props.answer.split())
    # Eliminate ``` from answer
    script_props.answer = script_props.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_props.answer = script_props.answer.replace("json", "")
    json_answer = json.loads(script_props.answer)
    merge_data.props = json_answer.get("props")

    return merge_data


def get_doc_gen_directors(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get character list
    script_directors = get_ai_director_recommendations(box_client, file)

    # Eliminate double spacing in answer
    script_directors.answer = " ".join(script_directors.answer.split())
    # Eliminate ``` from answer
    script_directors.answer = script_directors.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_directors.answer = script_directors.answer.replace("json", "")
    json_answer = json.loads(script_directors.answer)
    merge_data.directors = json_answer

    return merge_data


def get_doc_gen_producers(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get character list
    script_producers = get_ai_producer_recommendations(box_client, file)

    # Eliminate double spacing in answer
    script_producers.answer = " ".join(script_producers.answer.split())
    # Eliminate ``` from answer
    script_producers.answer = script_producers.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_producers.answer = script_producers.answer.replace("json", "")
    json_answer = json.loads(script_producers.answer)
    merge_data.producers = json_answer

    return merge_data
