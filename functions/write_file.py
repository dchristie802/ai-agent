import os
from google.genai import types

def write_file(working_directory, file_path, content):
  working_directory_abs = os.path.abspath(working_directory)
  target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
  valid_target_file_path = os.path.commonpath([target_file_path, working_directory_abs]) == working_directory_abs

  if not valid_target_file_path:
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  try:
    upsert = "x" if not os.path.exists(target_file_path) else "w"
    with open(target_file_path, upsert) as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to or creates the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write to or create, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write in the specified file path, relative to the working directory.",
            ),
        },
    ),
)
