import json

from box_sdk_gen import BoxClient, File

from .ai import (
    get_ai_character_list,
    get_ai_director_recommendations,
    get_ai_location_information,
    # get_ai_plot_summary,
    get_ai_producer_recommendations,
    get_ai_prop_list,
    get_ai_screen_writer,
    get_ai_script_data,
)
from .doc_gen_data_classes import CharacterList, MergeData, Movie, Script, Writer


def get_doc_gen_script_data(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    # Get script data
    script_data = get_ai_script_data(box_client, file)

    # Eliminate double spacing in answer
    script_data.answer = " ".join(script_data.answer.split())
    # print(script_data.answer)

    # TODO: Overwrite merge data with script data
    # This initial query picks up the characters list, and the summary
    script_data_dict = json.loads(script_data.answer)
    merge_data.script = Script.from_json(script_data.answer)

    return merge_data


# TODO: Dead code to remove
# def get_doc_gen_script_summary(
#     box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
# ) -> MergeData:
#     """Get the merge data for a file."""

#     # Get script summary
#     script_summary = get_ai_plot_summary(box_client, file)

#     # Eliminate double spacing in answer
#     script_summary.answer = " ".join(script_summary.answer.split())

#     merge_data.summary = script_summary.answer

#     return merge_data


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

    character_list = CharacterList.from_json(script_character_list.answer)
    merge_data.character_list = character_list.characters

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


def get_doc_gen_writer(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    xx = Writer()
    xx.other_scripts = ["", ""]
    xx.accomplishments = ["", ""]
    xx.produced_movies = [Movie(), Movie()]
    xx.companies_worked_with = ["", ""]

    print(xx.to_json())

    # Get character list
    script_producers = get_ai_screen_writer(box_client, file)

    # Eliminate double spacing in answer
    script_producers.answer = " ".join(script_producers.answer.split())
    # Eliminate ``` from answer
    script_producers.answer = script_producers.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_producers.answer = script_producers.answer.replace("json", "")

    json_answer = json.loads(script_producers.answer)
    writer = Writer.from_dict(json_answer)

    merge_data.screen_writer = writer

    return merge_data


def get_doc_gen_script_data_full(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Get the merge data for a file."""

    merge_data = get_doc_gen_script_data(box_client, file, merge_data)
    merge_data = get_doc_gen_script_summary(box_client, file, merge_data)
    merge_data = get_doc_gen_character_list(box_client, file, merge_data)
    merge_data = get_doc_gen_locations(box_client, file, merge_data)
    merge_data = get_doc_gen_props(box_client, file, merge_data)
    merge_data = get_doc_gen_directors(box_client, file, merge_data)
    merge_data = get_doc_gen_producers(box_client, file, merge_data)
    merge_data = get_doc_gen_writer(box_client, file, merge_data)

    return merge_data
