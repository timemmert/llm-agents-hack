import os

from backend.prompt_maker.make_prompt import conversation_buf


def text_for_name(name: str):
    path_of_this_python_folder = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(path_of_this_python_folder, f"../data/db/people/{name}.txt")

    with open(path, 'r') as file:
        content = file.read()
    return content

def prompt_from_name(name: str):
    return conversation_buf(
        text_for_name(name)
    )
