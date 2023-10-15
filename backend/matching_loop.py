import os

from backend.agent_conversation import converse
from backend.prompt_maker.make_prompt_from_name import prompt_from_name


def do_conversations_for_human(human_name: str):
    path_of_this_python_folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path_of_this_python_folder, f"data/db/people")

    conversation_partners_score = {}

    files = os.listdir(path)
    for file in files:
        name = file.split(".")[0]
        if name == human_name:
            continue
        conversation_partners_score[name] = {
            "score": 0,
            "description": "",
        }
        prompt_conversation_partner = prompt_from_name(name)
        prompt_conversation_current_human = prompt_from_name(human_name)

        messages = converse(prompt_conversation_partner['response'], prompt_conversation_current_human['response'])
        # TODO: Plug matching results into evaluator
        # conversation_partners_score = ...
    return conversation_partners_score


print(do_conversations_for_human("tim"))