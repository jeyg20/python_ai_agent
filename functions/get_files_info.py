import os


def format_file_info(item):
    return f"- {os.path.basename(item)}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}"


def get_files_info(working_directory: str, directory: str | None = None):

    try:
        working_directory = os.path.abspath(working_directory)
        if not os.path.isdir(working_directory):
            return f"Error: {working_directory} is not a directory"

        target_directory = os.path.join(working_directory, directory) if directory else working_directory
        target_directory = os.path.abspath(target_directory)

        if not target_directory.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        dir_names = os.listdir(target_directory)

        full_item_path = [os.path.join(target_directory, name) for name in dir_names]

        formatted_info_list = [format_file_info(item_path) for item_path in full_item_path]

        return "\n".join(formatted_info_list)

    except FileNotFoundError:
        return "Error: A path component was not found during processing."
    except Exception as e:
        return f"Error: {e}"
