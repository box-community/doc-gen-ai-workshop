import os

from box_sdk_gen import (
    BoxAPIError,
    BoxClient,
    CreateFolderParent,
    File,
    Folder,
    PreflightFileUploadCheckParent,
    UploadFileAttributes,
    UploadFileAttributesParentField,
    UploadUrl,
)


def create_folder(
    client: BoxClient,
    folder_name: str,
    parent_folder: Folder,
) -> Folder:
    """Create a folder in Box"""
    try:
        return client.folders.create_folder(
            folder_name, CreateFolderParent(parent_folder.id)
        )
    except BoxAPIError as e:
        if (
            e.response_info.status_code == 409
            and e.response_info.code == "item_name_in_use"
        ):
            box_folder_id = e.response_info.context_info.get("conflicts")[0].get("id")

            return client.folders.get_folder_by_id(box_folder_id)
        else:
            raise e


def upload_file(
    client: BoxClient,
    local_file_path,
    box_parent_folder: Folder,
    ignore_if_exists: bool = True,
) -> File:
    """Upload a file to Box"""
    # check if file exists locally and get the filename and size
    file_name = os.path.basename(local_file_path)
    file_size = os.path.getsize(local_file_path)

    upload_file_attributes = UploadFileAttributes(
        file_name,
        parent=UploadFileAttributesParentField(id=box_parent_folder.id),
    )

    # preflight check
    try:
        client.uploads.preflight_file_upload_check(
            name=file_name,
            size=file_size,
            parent=PreflightFileUploadCheckParent(id=box_parent_folder.id),
        )

        with open(local_file_path, "rb") as local_file_stream:
            box_file = client.uploads.upload_file(
                attributes=upload_file_attributes, file=local_file_stream
            )
            return box_file.entries[0]

    except BoxAPIError as e:
        if (
            e.response_info.status_code == 409
            and e.response_info.code == "item_name_in_use"
        ):
            box_file_id = e.response_info.context_info.get("conflicts").get("id")
            if ignore_if_exists:
                return client.files.get_file_by_id(box_file_id)

        else:
            raise e

    with open(local_file_path, "rb") as local_file_stream:
        return client.uploads.upload_file_version(
            box_file_id, upload_file_attributes, local_file_stream
        ).entries[0]
