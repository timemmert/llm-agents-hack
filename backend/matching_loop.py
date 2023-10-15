import os

from backend.agent_conversation import converse
from backend.prompt_maker.make_prompt_from_name import prompt_from_name
from evaluation.chain import compatibility_parser


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

        conversation = converse(
            prompt_conversation_current_human["response"],
            prompt_conversation_partner["response"],
        )

        # TODO: Plug matching results into evaluator
        conversation_partners_score = compatibility_parser(
            prompt_conversation_current_human, conversation
        )

    highest_score = -1
    highest_score_name = ""
    for name in conversation_partners_score:
        if highest_score < conversation_partners_score[name]["score"]:
            highest_score = conversation_partners_score[name]["score"]
            highest_score_name = name
        print(f"{name}: {conversation_partners_score[name]}")
    return highest_score_name, highest_score, conversation_partners_score[name]["description"]


print(do_conversations_for_human("tim"))
