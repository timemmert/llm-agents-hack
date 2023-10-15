from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage

from output_parsers import compatibility_parser, conversation_parser

# List of conversation histories
# Summarize each conversation, with pros and cons - using person model
# Take a list of summaries, pros, and cons, and generate a unified list - using ranked model

def summarize_conversation(person_prompt, conversation, verbose=False):
    try:
        conversation_history = conversation.memory.chat_memory.messages
    except:
        conversation_history = conversation

    messages = [
        SystemMessage(content=person_prompt),
    ] + list(conversation_history) + [
        SystemMessage(content=f"Now that you've had a conversation with another person, think about how you would feel if you were dating them. Summarize how romantically compatible you feel with them, both in free-form text, and as a list of pros and cons.\n\n{conversation_parser.get_format_instructions()}")
    ]

    chain = (
        ChatPromptTemplate.from_messages(messages)
        | ChatOpenAI()
        | conversation_parser
    )

    summary = chain.invoke({
        "format_instructions": conversation_parser.get_format_instructions()
    })

    if verbose:
        print(f"Got summary of conversation: {summary}")

    return summary

final_compatibility = (
    ChatPromptTemplate.from_messages([
        ("human", "{summaries}"),
        ("system", "Judge the romantic compatibility of two people from the list of summaries of conversations, pros, and cons written by one of the people in the conversation. Merge the pros and cons list into a distilled list of pros and cons, sorted by most important first. Given these pros and cons, output compatibility scores between 0 and 10 in specific categories. In general, the average score between two people should be about 5. A score of 10 implies the two are soulmates, while a score of 0 means that there is no fit.\n\n{format_instructions}"),
    ])
    | ChatOpenAI()
    | compatibility_parser
)

def final_compatibility_parse(summaries):
    return final_compatibility.invoke({
        "format_instructions": compatibility_parser.get_format_instructions(),
        "summaries": summaries
    })

def evaluate_compatibility(person_prompt, conversation_list, verbose=False):
    # this could be parallelized, especially with nice langchain tools
    # unfortunately, it's easier to do it serially first...
    summaries = [summarize_conversation(person_prompt, conversation, verbose=verbose) for conversation in conversation_list]
    return final_compatibility_parse(summaries)
