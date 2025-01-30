from typing import List

from box_sdk_gen import (
    AiItemBase,
    AiItemBaseTypeField,
    AiResponseFull,
    BoxClient,
    CreateAiAskMode,
    File,
)

from .doc_gen_data_classes import Character, CharacterList, Location, Script

# TODO: Dead code to remove
# def get_ai_plot_summary(client: BoxClient, box_file: File) -> AiResponseFull:
#     """
#     Get AI plot summary of a Box file.
#     """
#     mode = CreateAiAskMode.SINGLE_ITEM_QA
#     prompt = "read this movie script and summarize the plot, ignoring if the movie has been already produced"
#     item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
#     return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_character_list(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI character list of a Box file.
    """
    # TODO: Flaky schemas
    # characters = CharacterList()
    # schema = characters.json_schema()
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and give me a character list, "
        # f"compose this characters list in a json format using this json schema: {schema}"
        "(without the original actor name, just the character name) "
        "with one sentence description "
        "and suggest 5 actors for each character "
        "do not suggest the original movie actors if the movie has been already produced. "
        "compose this characters list in a json format "
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_location_information(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI location information of a Box file.
    """
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and give me a list of locations "
        "with one sentence description for each location "
        "do not suggest the original movie locations if the movie has been already produced. "
        "compose this locations list in a json format "
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_prop_list(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI prop list of a Box file.
    """
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and give me a list of props "
        "with one sentence description for each prop. "
        "compose this props list in a json format "
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_director_recommendations(
    client: BoxClient, box_file: File
) -> AiResponseFull:
    """
    Get AI director recommendations of a Box file.
    """
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and provide  me a list of your recommended directors "
        "with one sentence description for each director "
        "do not suggest the original movie director if the movie has been already produced. "
        "compose this directors list in a json format "
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_producer_recommendations(
    client: BoxClient, box_file: File
) -> AiResponseFull:
    """
    Get AI producer recommendations of a Box file.
    """
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and provide  me a list of your recommended producers "
        "with one sentence description for each producer "
        "do not suggest the original movie producer if the movie has been already produced. "
        "compose this producers list in a json format "
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_screen_writer(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI screen writer of a Box file.
    """
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and provide me information on the screen writer "
        "include other scrips the screen writer has written "
        "and a summary of accomplishments. "
        "If the screen writer does have movies that were produced, "
        "Include a separate bullet list summary of grossed revenue for each past movie. "
        "Include a separate bullet list of the companies the screen writer has worked with. "
        "compose this information in json using this format: "
        '{"name": "", "accomplishments": ["", ""], "other_scripts": ["", ""], "produced_movies": [{"title": "", "gross_revenue": ""}, {"title": "", "gross_revenue": ""}], "companies_worked_with": ["", ""]}'
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_script_data(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI script data of a Box file.
    """
    script_schema = Script().json_schema()

    prompt = (
        f"Retrieve the following data from the movie script: {script_schema}"
        # "Title, "
        # "Author, "
        # "Genre, "
        # "Date written. "
        # f"using this json schema: {schema}"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_extract(prompt, [item])
