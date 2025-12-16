import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

MAX_ITERATIONS = 20

def main():
    if api_key == None:
        raise RuntimeError

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ],
    )

    curr_iteration = 0
    while curr_iteration < MAX_ITERATIONS:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                )
            )

            # Keep track of conversation
            for candidate in response.candidates:
                messages.append(candidate.content)

            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            function_responses = []
            if response.function_calls:
                for function_call in response.function_calls:
                    call_result = call_function(function_call, verbose=args.verbose)

                    if call_result.parts and call_result.parts[0].function_response:
                        function_responses.append(call_result.parts[0])

                    if args.verbose:
                        print(f"-> {call_result.parts[0].function_response.response}")

                messages.append(types.Content(role="user", parts=function_responses))

            else:
                if response.text:
                    print(f"Final response:\n{response.text}")
                    break
                else:
                    pass

            curr_iteration += 1
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    main()
