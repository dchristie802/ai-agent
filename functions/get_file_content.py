import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
  working_dir_abs = os.path.abspath(working_directory)
  target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
  valid_target_file_path = os.path.commonpath([target_file_path, working_dir_abs]) == working_dir_abs

  if not valid_target_file_path:
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

  if not os.path.isfile(target_file_path):
    return f'Error: File not found or is not a regular file: "{file_path}"'

  try:
    with open(target_file_path, "r") as f:
      file_content_string = f.read(MAX_CHARS)

      # print(len(file_content_string))

      if len(file_content_string) == MAX_CHARS:
        return file_content_string + f' [...File "{file_path}" truncated at 10000 characters]'

      return file_content_string
  except Exception as e:
    return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads files in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read from, relative to the working directory.",
            ),
        },
    ),
)
