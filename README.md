# Automating document analysis with Box AI and Document Generation

This project is a workshop for generating documents using AI and the Box API. It includes scripts for initializing the environment, processing a single document, and merging documents.

## Pre-requisites and guides

This workshop assumes you are somewhat familiar with the Box API, Box Applications, and types of authentication supported.


For more information on topics related to this workshop, take a look at:

- [Getting started](https://developer.box.com/guides/getting-started/)
- [Authentication](https://developer.box.com/guides/authentication/)
- [Box AI](https://developer.box.com/guides/box-ai/)
- [Box Doc Gen](https://developer.box.com/guides/docgen/)

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/box-community/doc-gen-ai-workshop.git
    cd doc-gen-ai-workshop
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the following environment variables:

    ```env
    BOX_CLIENT_ID=your_box_client_id
    BOX_CLIENT_SECRET=your_box_client_secret
    BOX_ENTERPRISE_ID=your_box_enterprise_id
    BOX_USER_ID=your_box_user_id
    BOX_WORKSHOP_PARENT_FOLDER_ID=your_box_workshop_parent_folder_id
    ```
    This assumes you have created a Box application, configured to use Client Credential Grant (CCG), have Box AI and Doc Gen enabled. 

## Initial Run Instructions

1. **Run [init.py](src/init.py) to set up the Box folder structure and upload the template:**

    ```sh
    python src/init.py
    ```

    This script will create the necessary folder structure in your Box account and upload the template file.


2. **Run [ai_single_document.py](src/ai_single_document.py) to process a single document:**

    ```sh
    python src/ai_single_document.py
    ```

    This script will select a random movie script from the Box folder, process it using AI, and save the generated data to a JSON file in the [output](output/) folder.

3. **Run [merge_single_document.py](src/merge_single_document.py) to merge the processed document:**

    ```sh
    python src/merge_single_document.py
    ```

    This script will merge the processed document data into a single PDF file using the Box API.

## Additional Information

- The [ai_all_documents.py](src/ai_all_documents.py) script can be used to process all documents in the Box folder.
- The [merge_all_documents.py](src/merge_all_documents.py) script can be used to merge all processed documents into a single PDF file.

For more details, refer to the source code and comments within each script.

## Code guide

### `src/api/ai.py`
This file contains functions to interact with AI services. It includes functions to get AI-generated data for scripts, such as character lists, director recommendations, producer recommendations, and more. The main functions are:
- `get_ai_character_list`: Retrieves a list of characters from a script.
- `get_ai_director_recommendations`: Retrieves a list of recommended directors.
- `get_ai_producer_recommendations`: Retrieves a list of recommended producers.
- `get_ai_script_data_extract`: Extracts script data using AI.
- `get_ai_smart_load`: Retrieves comprehensive AI-generated data for a script.

### `src/api/doc_gen.py`
This file contains functions to generate document data using AI. It includes functions to get various types of data from AI and merge them into a script object. The main functions are:
- `get_doc_gen_script_data`: Retrieves basic script data from AI.
- `get_doc_gen_character_list`: Retrieves a list of characters from AI.
- `get_doc_gen_directors`: Retrieves a list of directors from AI.
- `get_doc_gen_producers`: Retrieves a list of producers from AI.
- `get_doc_gen_smart_load`: Retrieves comprehensive data including directors, producers, and more.
- `get_doc_gen_script_data_full`: Retrieves all available data from AI and merges it into a script object.

### `src/api/doc_gen_data_classes.py`
This file contains data classes used in the document generation process. These classes define the structure of the data used in the scripts. The main classes are:
- `MergeBase`: Base class for all data classes.
- `GenericNameDescription`: Class for objects with a name and description.
- `GenericDescription`: Class for objects with a description.
- `Movie`: Class representing a movie with a title and gross revenue.
- `Accomplishment`: Class representing an accomplishment.
- `OtherScript`: Class representing another script.
- `CompanyWorked`: Class representing a company worked with.
- `Producer`: Class representing a producer.
- `Director`: Class representing a director.
- `Prop`: Class representing a prop.
- `Location`: Class representing a location.
- `Character`: Class representing a character.
- `Script`: Class representing a script with various attributes like title, author, genre, plot summary, etc.