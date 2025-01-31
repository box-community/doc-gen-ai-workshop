import json

from box_sdk_gen import BoxClient, File

from .ai import (
    get_ai_character_list,
    get_ai_director_recommendations,
    get_ai_producer_recommendations,
    get_ai_screen_writer,
    get_ai_script_data_extract,
    get_ai_smart_load,
)
from .doc_gen_data_classes import (
    Character,
    Director,
    MergeData,
    Producer,
    Script,
    Writer,
)


def get_doc_gen_script_data(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """returns the script data from the AI"""

    # Get script data
    script_data = get_ai_script_data_extract(box_client, file)

    # Eliminate double spacing in answer
    script_data.answer = " ".join(script_data.answer.split())

    # Eliminate \\" from answer and replace by '
    script_data.answer = script_data.answer.replace('\\"', "'")

    script_data_dict = json.loads(script_data.answer)

    merge_data.script = Script.from_json(script_data.answer)

    return merge_data


def get_doc_gen_character_list(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Returns the character list from the AI"""

    # Get character list
    script_character_list = get_ai_character_list(box_client, file)

    # Eliminate double spacing in answer
    script_character_list.answer = " ".join(script_character_list.answer.split())
    # Eliminate ``` from answer
    script_character_list.answer = script_character_list.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_character_list.answer = script_character_list.answer.replace("json", "")

    character_list = Character.schema().loads(script_character_list.answer, many=True)
    merge_data.character_list = character_list

    return merge_data


def get_doc_gen_directors(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Returns the director list from the AI"""

    # Get character list
    script_directors = get_ai_director_recommendations(box_client, file)

    # Eliminate double spacing in answer
    script_directors.answer = " ".join(script_directors.answer.split())
    # Eliminate ``` from answer
    script_directors.answer = script_directors.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_directors.answer = script_directors.answer.replace("json", "")

    directors = Director.schema().loads(script_directors.answer, many=True)
    merge_data.directors = directors

    return merge_data


def get_doc_gen_producers(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Returns the producer list from the AI"""

    # Get character list
    script_producers = get_ai_producer_recommendations(box_client, file)

    # Eliminate double spacing in answer
    script_producers.answer = " ".join(script_producers.answer.split())
    # Eliminate ``` from answer
    script_producers.answer = script_producers.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_producers.answer = script_producers.answer.replace("json", "")

    producers = Producer.schema().loads(script_producers.answer, many=True)
    merge_data.producers = producers

    return merge_data


def get_doc_gen_writer(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Returns the writer from the AI"""

    script_writer = get_ai_screen_writer(box_client, file)

    # Eliminate double spacing in answer
    script_writer.answer = " ".join(script_writer.answer.split())
    # Eliminate ``` from answer
    script_writer.answer = script_writer.answer.replace("```", "")
    # Eliminate the word json form from answer
    script_writer.answer = script_writer.answer.replace("json", "")
    script_writer_dict = json.loads(script_writer.answer)
    script_writer_dict = script_writer_dict.get("Writer")
    writer = Writer.from_dict(script_writer_dict)
    merge_data.screen_writer = writer

    return merge_data


def get_doc_gen_smart_load(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Returns directors, producers and writer data from the AI"""

    ai_answer = get_ai_smart_load(box_client, file)

    # Eliminate double spacing in answer
    ai_answer.answer = " ".join(ai_answer.answer.split())
    # Eliminate ``` from answer
    ai_answer.answer = ai_answer.answer.replace("```", "")
    # Eliminate the word json form from answer
    ai_answer.answer = ai_answer.answer.replace("json", "")

    answer_dict = json.loads(ai_answer.answer)
    # print(answer_dict)

    director_list = json.dumps(answer_dict.get("directors"))
    producer_list = json.dumps(answer_dict.get("producers"))
    directors = Director.schema().loads(director_list, many=True)
    producers = Producer.schema().loads(producer_list, many=True)
    writer = Writer.from_dict(answer_dict.get("writer"))

    merge_data.directors = directors
    merge_data.producers = producers
    merge_data.screen_writer = writer

    return merge_data


def get_doc_gen_script_data_full(
    box_client: BoxClient, file: File, merge_data: MergeData = MergeData()
) -> MergeData:
    """Returns all the data from the AI"""

    merge_data = get_doc_gen_script_data(box_client, file, merge_data)
    merge_data = get_doc_gen_character_list(box_client, file, merge_data)
    merge_data = get_doc_gen_smart_load(box_client, file, merge_data)

    return merge_data
