from langchain.chains import ConversationChain
from langchain.llms.openai import OpenAI
from pymongo.collection import Collection
from langchain.memory import ConversationBufferMemory



def mock_langchain(name: str):
    pass

def matching():
    # Data we get: Name
    # TODO: given Nikhils function, generate LangChain agents

    # TODO: iterate over all agents
    # Nikhil gives me the system prompt
    llm_one = OpenAI(temperature=0, openai_api_key="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", system=)
    llm_two = OpenAI(temperature=0, openai_api_key="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")
    conversation = converse(llm_one, llm_two, initial_prompt)  # Initial promt might be


def converse(llm_one, llm_two):
    """
    Given two LLMs, this returns the conversation.

    :param llm_one:
    :param llm_two:
    :return:
    """
    conversation_one = ConversationChain(
        llm=llm_one,
        verbose=True,
        memory=ConversationBufferMemory()
    )
    conversation_two = ConversationChain(
        llm=llm_two,
        verbose=True,
        memory=ConversationBufferMemory()
    )
    output_two = "Hi there!"
    # System: those are my intersts -> system message for both of them
    for i in range(3):
        output_one = conversation_one.predict(input=output_two)
        output_two = conversation_two.predict(input=output_one)
    messages = conversation_one.memory.buffer_as_messages  # TODO: right now, misses last message
    return messages
