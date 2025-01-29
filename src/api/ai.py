from box_sdk_gen import (
    AiItemBase,
    AiItemBaseTypeField,
    AiResponseFull,
    BoxClient,
    CreateAiAskMode,
    File,
)


def get_ai_plot_summary(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI plot summary of a Box file.
    """
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = "read this movie script and summarize the plot, ignoring if the movie has been already produced"
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_character_list(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI character list of a Box file.
    """
    mode = CreateAiAskMode.SINGLE_ITEM_QA
    prompt = (
        "read this movie script and give me a character list, "
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
        "do not suggest the original movie locations if the movie has been already produced"
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
        "with one sentence description for each prop "
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
        "do not suggest the original movie director if the movie has been already produced"
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
        "do not suggest the original movie producer if the movie has been already produced"
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
        "If the screen writer does have movies being produced, "
        "include a bullet list summary of grossed revenue for each movie on a separate paragraph. "
        "On another paragraph, include a bullet list of the companies the screen writer has worked with. "
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_ask(mode, prompt, [item])


def get_ai_script_data(client: BoxClient, box_file: File) -> AiResponseFull:
    """
    Get AI script data of a Box file.
    """
    prompt = (
        "retrieve the following data from the movie script: "
        "Title, "
        "Author, "
        "Genre, "
        "Date written"
    )
    item = AiItemBase(id=box_file.id, type=AiItemBaseTypeField.FILE)
    return client.ai.create_ai_extract(prompt, [item])
