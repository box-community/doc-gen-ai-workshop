from box_sdk_gen import (
    AiItemBase,
    AiItemBaseTypeField,
    AiResponseFull,
    BoxClient,
    CreateAiAskMode,
    File,
)

from .doc_gen_data_classes import (
    Character,
    Director,
    Location,
    Producer,
    Prop,
    Script,
    Writer,
)


def get_ai_character_list(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI character list of a Box file.
    """
    sample_json_object = [
        Character(name="Character Name", description="Character Description")
    ]
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and give me a character list, "
        "(without the original actor name, just the character name) "
        "with one sentence description "
        "and suggest 5 actors for each character "
        "do not suggest the original movie actors if the movie has been already produced. "
        f"format the output this directors list in a json format using this example: {sample_json_object}"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_director_recommendations(
    client: BoxClient, box_file: File
) -> AiResponseFull:
    """
    Get AI director recommendations of a Box file.
    """
    sample_json_object = [
        Director(name="Director name", description="Director description")
    ]

    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and provide  me a list of your recommended directors "
        "with one sentence description for each director "
        "do not suggest the original movie director if the movie has been already produced. "
        f"format the output this directors list in a json format using this example: {sample_json_object}"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_producer_recommendations(
    client: BoxClient, box_file: File
) -> AiResponseFull:
    """
    Get AI producer recommendations of a Box file.
    """
    sample_json_object = [
        Producer(name="Director name", description="Director description")
    ]
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and provide  me a list of your recommended producers "
        "with one sentence description for each producer "
        "do not suggest the original movie producer if the movie has been already produced. "
        f"format the output this directors list in a json format using this example: {sample_json_object}"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_screen_writer(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI screen writer of a Box file.
    """
    sample_json_object = Writer(name="Writer Name")
    sample_json_object.accomplishments = ["Accomplishment 1", "Accomplishment 2"]
    sample_json_object.other_scripts = ["Script 1", "Script 2"]
    sample_json_object.produced_movies = [
        {"title": "Movie 1", "gross_revenue": "1000000"},
        {"title": "Movie 2", "gross_revenue": "2000000"},
    ]
    sample_json_object.companies_worked_with = ["Company 1", "Company 2"]

    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and provide me information on the script writer "
        "include other scrips the screen writer has written "
        "and a summary of accomplishments. "
        "If the screen writer does have movies that were produced, "
        "Include a separate bullet list summary of grossed revenue for each past movie. "
        "Include a separate bullet list of the companies the screen writer has worked with. "
        f"format the output this directors list in a json format using this example: {sample_json_object}"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_smart_load(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI smart load of a Box file.
    """
    directors = [Director(name="Director name", description="Director description")]

    producers = [Producer(name="Director name", description="Director description")]

    writer = Writer(name="Writer Name")
    writer.accomplishments = ["Accomplishment 1", "Accomplishment 2"]
    writer.other_scripts = ["Script 1", "Script 2"]
    writer.produced_movies = [
        {"title": "Movie 1", "gross_revenue": "1000000"},
        {"title": "Movie 2", "gross_revenue": "2000000"},
    ]
    writer.companies_worked_with = ["Company 1", "Company 2"]

    locations = [Location(name="Location Name", description="Location Description")]
    props = [Prop(name="Prop Name", description="Prop Description")]

    sample_dict = {}
    sample_dict["directors"] = directors
    sample_dict["producers"] = producers
    sample_dict["writer"] = writer
    sample_dict["locations"] = locations
    sample_dict["props"] = props

    mode = CreateAiAskMode.SINGLE_ITEM_QA

    prompt = (
        "read this movie script and provide  me with the following:"
        # Directors
        "Recommended Directors: Suggest a list of 5 of your recommended directors "
        "with one sentence description for each director "
        "do not suggest the original movie director if the movie has been already produced. "
        # Producers
        "Recommended Producers: Suggest a list of 5 of your recommended producers "
        "with one sentence description for each producer "
        "do not suggest the original movie producer if the movie has been already produced. "
        # Screen Writer
        "Script Writer: information on the script writer "
        "include other scrips the screen writer has written "
        "and a summary of accomplishments. "
        "If the screen writer does have movies that were produced, "
        "Include a separate bullet list summary of grossed revenue for each past movie. "
        "Include a separate bullet list of the companies the screen writer has worked with. "
        # Locations
        "Locations: Provide a list of up to 10 locations "
        "with a one sentence description for each location. "
        # Props
        "Props: Provide a list of up to 10 props "
        "with a one sentence description for each prop. "
        # Format
        f"format the output this directors list in a json format using this example: {sample_dict}"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_script_data_extract(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI script data of a Box file.
    """

    script_schema = Script().json_schema()
    # # Add min max elements to locations
    # script_schema["allOf"][1]["properties"]["locations"]["minItems"] = 1
    # script_schema["allOf"][1]["properties"]["locations"]["maxItems"] = 10

    # # # Add min max elements to props
    # script_schema["allOf"][1]["properties"]["props"]["minItems"] = 1
    # script_schema["allOf"][1]["properties"]["props"]["maxItems"] = 10

    # The AI seems to be hallucinating for locations and props
    # so we will remove them from the schema and put them in the aks endpoint
    # checking if locations and props exist in the schema

    properties = script_schema["allOf"][1]["properties"]

    if "locations" in properties:
        properties.pop("locations")

    if "props" in properties:
        properties.pop("props")

    prompt = f"{script_schema}"
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_extract(prompt, [item])
