import os
import subprocess


def _resolve_and_validate_path(working_directory: str, target_path: str, ensure_dirs_exist: bool = False):
    """
    Resolves and validates a path within a working directory.
    Returns (resolved_path, error_message) where error_message is None if valid.
    """
    working_directory = os.path.abspath(working_directory)

    if os.path.isabs(target_path):
        resolved_path = os.path.abspath(target_path)
    else:
        resolved_path = os.path.abspath(os.path.join(working_directory, target_path))

    if ensure_dirs_exist:
        dir_parts = os.path.dirname(target_path)
        if not os.path.exists(os.path.dirname(resolved_path)):
            os.makedirs(dir_parts)

    if not resolved_path.startswith(working_directory):
        return None, True

    return resolved_path, False


def format_file_info(item):
    return f"- {os.path.basename(item)}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}"


def get_files_info(working_directory: str, directory: str | None = None):
    resolved_path, error = _resolve_and_validate_path(working_directory, directory)

    if error:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(resolved_path):
        return f'Error: "{directory}" is not a directory'

    try:
        dir_names = os.listdir(resolved_path)

        full_item_path = [os.path.join(resolved_path, name) for name in dir_names]

        formatted_info_list = [format_file_info(item_path) for item_path in full_item_path]

        return "\n".join(formatted_info_list)

    except Exception as e:
        return f"Error: {e}"


MAX_CHARS = 10_000


def get_file_content(working_directory: str, file_path: str) -> str:
    resolved_path, error = _resolve_and_validate_path(working_directory, file_path)

    if error:
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(resolved_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(resolved_path, "r", encoding="utf-8") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'\n[...File "{file_path}" truncated at 10000 characters]'

        return file_content

    except Exception as e:
        return f"Error: {e}"


def write_file(working_directory: str, file_path: str, content: str) -> str:
    resolved_path, error = _resolve_and_validate_path(working_directory, file_path, True)

    if error:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(resolved_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
