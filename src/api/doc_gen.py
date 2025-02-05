import json

from box_sdk_gen import BoxClient, File

from .ai import (
    get_ai_character_list,
    get_ai_director_recommendations,
    get_ai_producer_recommendations,
    get_ai_script_data_extract,
    get_ai_smart_load,
)
from .doc_gen_data_classes import (
    Accomplishment,
    Character,
    CompanyWorked,
    Director,
    Location,
    Movie,
    OtherScript,
    Producer,
    Script,
)


def get_doc_gen_script_data(
    box_client: BoxClient, file: File, merge_data: Script = None
) -> Script:
    """returns the script data from the AI"""

    # Get script data
    script_data = get_ai_script_data_extract(box_client, file)

    # Eliminate double spacing in answer
    script_data.answer = " ".join(script_data.answer.split())

    # Eliminate ``` from answer
    script_data.answer = script_data.answer.replace("```", "")

    # Eliminate the word json form from answer
    script_data.answer = script_data.answer.replace("json", "")

    # Eliminate \\" from answer and replace by '
    script_data.answer = script_data.answer.replace('\\"', "'")

    script_data_dict = json.loads(script_data.answer)

    if merge_data is None:
        merge_data = Script()

    merge_data.title = script_data_dict.get("title")
    merge_data.author = script_data_dict.get("author")
    merge_data.genre = script_data_dict.get("genre")
    merge_data.date_written = script_data_dict.get("date_written")
    merge_data.date_written_iso = script_data_dict.get("date_written_iso")
    merge_data.plot_summary = script_data_dict.get("plot_summary")

    return merge_data


def get_doc_gen_character_list(
    box_client: BoxClient, file: File, merge_data: Script = None
) -> Script:
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

    if merge_data is None:
        merge_data = Script()

    merge_data.character_list = character_list

    return merge_data


def get_doc_gen_directors(
    box_client: BoxClient, file: File, merge_data: Script = None
) -> Script:
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

    if merge_data is None:
        merge_data = Script()

    merge_data.directors = directors

    return merge_data


def get_doc_gen_producers(
    box_client: BoxClient, file: File, merge_data: Script = None
) -> Script:
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
    if merge_data is None:
        merge_data = Script()
    merge_data.producers = producers

    return merge_data


def get_doc_gen_smart_load(
    box_client: BoxClient, file: File, merge_data: Script = None
) -> Script:
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
    location_list = json.dumps(answer_dict.get("locations"))
    prop_list = json.dumps(answer_dict.get("props"))
    accomplishments_list = json.dumps(answer_dict.get("accomplishments"))
    other_scripts_list = json.dumps(answer_dict.get("other_scripts"))
    produced_movies_list = json.dumps(answer_dict.get("produced_movies"))
    companies_worked_with_list = json.dumps(answer_dict.get("companies_worked_with"))

    directors = Director.schema().loads(director_list, many=True)
    producers = Producer.schema().loads(producer_list, many=True)
    # writer = Writer.from_dict(answer_dict.get("writer"))
    locations = Location.schema().loads(location_list, many=True)
    props = Location.schema().loads(prop_list, many=True)
    accomplishments = Accomplishment.schema().loads(accomplishments_list, many=True)
    other_scripts = OtherScript.schema().loads(other_scripts_list, many=True)
    produced_movies = Movie.schema().loads(produced_movies_list, many=True)
    companies_worked_with = CompanyWorked.schema().loads(
        companies_worked_with_list, many=True
    )

    if merge_data is None:
        merge_data = Script()

    merge_data.plot_summary = answer_dict.get("plot_summary")
    merge_data.directors = directors
    merge_data.producers = producers
    merge_data.locations = locations
    merge_data.props = props
    merge_data.locations = locations
    merge_data.accomplishments = accomplishments
    merge_data.other_scripts = other_scripts
    merge_data.produced_movies = produced_movies
    merge_data.companies_worked_with = companies_worked_with

    return merge_data


def get_doc_gen_script_data_full(
    box_client: BoxClient, file: File, merge_data: Script = None
) -> Script:
    """Returns all the data from the AI"""

    if merge_data is None:
        merge_data = Script()

    merge_data = get_doc_gen_script_data(box_client, file, merge_data)
    merge_data = get_doc_gen_character_list(box_client, file, merge_data)
    merge_data = get_doc_gen_smart_load(box_client, file, merge_data)

    return merge_data
