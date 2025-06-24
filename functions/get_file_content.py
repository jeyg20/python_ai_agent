import os

MAX_CHARS = 10_000


def get_file_content(working_directory: str, file_path: str):
    try:
        working_directory = os.path.abspath(working_directory)
        if not os.path.isdir(working_directory):
            return f"Error: {working_directory} is not a directory"

        target_file = os.path.join(working_directory, file_path) if file_path else working_directory
        target_file = os.path.abspath(target_file)

        if not target_file.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r", encoding="utf-8") as f:
            file_content = f.read()
            if len(file_content) > MAX_CHARS:
                file_content = file_content + "\n" + f' [...File "{file_path}" truncated at 10000 characters]'

        return file_content

    except FileNotFoundError:
        return "Error: A path component was not found during processing."
    except Exception as e:
        return f"Error: {e}"
