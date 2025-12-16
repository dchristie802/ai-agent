import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
  working_dir_abs = os.path.abspath(working_directory)
  target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
  valid_target_file_path = os.path.commonpath([target_file_path, working_dir_abs]) == working_dir_abs

  if not valid_target_file_path:
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

  if not os.path.isfile(target_file_path):
    return f'Error: File "{file_path}" not found.'

  if not file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'

  try:
    completed_process = subprocess.run(
        args=["python3", file_path] + args,
        capture_output=True,
        text=True,
        cwd=working_dir_abs,
        timeout=30
      )

    if not completed_process.stdout and not completed_process.stderr:
      return "No output produced"

    result = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

    if completed_process.returncode != 0:
      result += f"\nProcess exited with code {completed_process.returncode}"

    return result
  except Exception as e:
    return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python files in the file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
              type=types.Type.ARRAY,
              items=types.Schema(
                  type=types.Type.STRING
              ),
              description="A list of optional arguments when running the subprocess. Arguments [\"python3\", <file_path>] will always be included",
            )
        },
    ),
)
