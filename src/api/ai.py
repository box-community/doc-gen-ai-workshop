from box_sdk_gen import (
    AiItemBase,
    AiItemBaseTypeField,
    AiResponseFull,
    BoxClient,
    CreateAiAskMode,
    File,
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
    Prop,
    Script,
)


def get_ai_character_list(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI character list of a Box file.
    """
    sample_json_object = [Character.gen_sample_data()]

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


def get_ai_smart_load(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI smart load of a Box file.
    """
    plot_summary = ""
    directors = [Director("Director name", "Director description")]

    producers = [Producer("Director name", "Director description")]

    accomplishments = [
        Accomplishment("Accomplishment 1"),
        Accomplishment("Accomplishment 2"),
    ]
    other_scripts = [
        OtherScript("Script 1"),
        OtherScript("Script 2"),
    ]
    produced_movies = [
        Movie("Movie 1", "1000000"),
        Movie("Movie 2", "2000000"),
    ]
    companies_worked_with = [
        CompanyWorked("Company 1"),
        CompanyWorked("Company 2"),
    ]

    locations = [Location("Location Name", "Location Description")]
    props = [Prop("Prop Name", "Prop Description")]

    sample_dict = {}
    sample_dict["directors"] = directors
    sample_dict["producers"] = producers
    sample_dict["locations"] = locations
    sample_dict["props"] = props
    sample_dict["accomplishments"] = accomplishments
    sample_dict["other_scripts"] = other_scripts
    sample_dict["produced_movies"] = produced_movies
    sample_dict["companies_worked_with"] = companies_worked_with
    sample_dict["plot_summary"] = plot_summary

    mode = CreateAiAskMode.SINGLE_ITEM_QA

    prompt = (
        "read this movie script and provide  me with the following:"
        # Plot summary
        "Plot Summary: Provide a summary of the plot of this movie script. "
        # Directors
        "Recommended Directors: Suggest a list of 5 of your recommended directors "
        "with one sentence description for each director "
        "do not suggest the original movie director if the movie has been already produced. "
        # Producers
        "Recommended Producers: Suggest a list of 5 of your recommended producers "
        "with one sentence description for each producer "
        "do not suggest the original movie producer if the movie has been already produced. "
        # Locations
        "Locations: Provide a list of up to 10 locations "
        "with a one sentence description for each location. "
        # Props
        "Props: Provide a list of up to 10 props "
        "with a one sentence description for each prop. "
        # Accomplishments, Other scripts, Produced movies, Companies worked with
        "Other scripts: Provide a list of up to 5 scripts written by the author. "
        # Accomplishments
        "Accomplishments: Provide a list of up to 5 accomplishments from author. "
        # Produced movies
        "Produced Movies: Provide a list of up to 5 other movies associated with this author, "
        "including the grossed revenue for each past movie. "
        # Companies worked with
        "Companies Worked With: Provide a list of up to 5 companies the author has worked with. "
        # Format
        f"format the output list in a json format using this example: {sample_dict}"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_script_data_extract(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI script data of a Box file.
    """

    script_schema = Script().json_schema()
    properties = script_schema["allOf"][1]["properties"]

    if "plot_summary" in properties:
        properties.pop("plot_summary")
    if "locations" in properties:
        properties.pop("locations")
    if "props" in properties:
        properties.pop("props")
    if "directors" in properties:
        properties.pop("directors")
    if "producers" in properties:
        properties.pop("producers")
    if "accomplishments" in properties:
        properties.pop("accomplishments")
    if "other_scripts" in properties:
        properties.pop("other_scripts")
    if "produced_movies" in properties:
        properties.pop("produced_movies")
    if "companies_worked_with" in properties:
        properties.pop("companies_worked_with")

    prompt = f"{script_schema}"
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_extract(prompt, [item])
