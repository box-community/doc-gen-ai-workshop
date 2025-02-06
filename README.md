# doc-gen-ai-workshop

This project is a workshop for generating documents using AI and the Box API. It includes scripts for initializing the environment, processing a single document, and merging documents.

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

    Create a [.env](http://_vscodecontentref_/4) file in the root directory of the project and add the following environment variables:

    ```env
    BOX_CLIENT_ID=your_box_client_id
    BOX_CLIENT_SECRET=your_box_client_secret
    BOX_ENTERPRISE_ID=your_box_enterprise_id
    BOX_USER_ID=your_box_user_id
    BOX_WORKSHOP_PARENT_FOLDER_ID=your_box_workshop_parent_folder_id
    ```

## Initial Run Instructions

1. **Run [init.py](http://_vscodecontentref_/5) to set up the Box folder structure and upload the template:**

    ```sh
    python src/init.py
    ```

    This script will create the necessary folder structure in your Box account and upload the template file.

2. **Run [ai_single_document.py](http://_vscodecontentref_/6) to process a single document:**

    ```sh
    python src/ai_single_document.py
    ```

    This script will select a random movie script from the Box folder, process it using AI, and save the generated data to a JSON file in the [output](http://_vscodecontentref_/7) folder.

3. **Run [merge_single_document.py](http://_vscodecontentref_/8) to merge the processed document:**

    ```sh
    python src/merge_single_document.py
    ```

    This script will merge the processed document data into a single PDF file using the Box API.

## Additional Information

- The [ai_all_documents.py](http://_vscodecontentref_/9) script can be used to process all documents in the Box folder.
- The [merge_all_documents.py](http://_vscodecontentref_/10) script can be used to merge all processed documents into a single PDF file.

For more details, refer to the source code and comments within each script.