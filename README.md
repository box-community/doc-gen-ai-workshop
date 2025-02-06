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