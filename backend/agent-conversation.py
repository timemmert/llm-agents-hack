from langchain.chains import ConversationChain
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory


def mock_langchain(name: str):
    pass


def matching(person_1_description, person_2_description):
    llm_one = OpenAI(
        temperature=0,
        openai_api_key="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",
    )
    llm_two = OpenAI(
        temperature=0,
        openai_api_key="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",
    )
    system_description = """ You are having a conversation with another person whom you are meeting for the first time.
        Your goal is to be kind, friendly, and learn more about them. You are not an AI, but rather an individual
        with the following description:
        {}
        """
    template_rest = """
        When conversing, please keep your conversation aligned with this description. Reference particular facts
        about yourself from the description.
        Current conversation:
        {history}
        Human: {input}
        AI:"""
    return converse(
        llm_one,
        llm_two,
        person_1_description,
        person_2_description,
        system_description=system_description,
        template_rest=template_rest,
    )


def converse(
    llm_one,
    llm_two,
    person_1_description,
    person_2_description,
    system_description,
    template_rest,
):
    """
    Given two LLMs, this returns the conversation.

    :param llm_one:
    :param llm_two:
    :return:
    """
    conversation_1_prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=system_description.format(person_1_description) + template_rest,
    )
    conversation_2_prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=system_description.format(person_2_description) + template_rest,
    )

    conversation_one = ConversationChain(
        llm=llm_one,
        memory=ConversationBufferMemory(),
        prompt=conversation_1_prompt,
    )
    conversation_two = ConversationChain(
        llm=llm_two,
        memory=ConversationBufferMemory(),
        prompt=conversation_2_prompt,
    )
    output_two = "Hey there!"
    # print("2", output_two)
    for i in range(3):
        output_one = conversation_one.predict(
            input=output_two,
        )
        # print("1", output_one)
        output_two = conversation_two.predict(
            input=output_one,
        )
        # print("2", output_two)
    messages = (
        conversation_one.memory.buffer_as_messages
    )  # TODO: right now, misses last message
    return messages


person_1_description = "--------- Passionate about computer vision and animal rights----- BS/MS student at Stanford----- Enjoys reading, hiking, and playing video games----- Values honesty, integrity, and hard work----- Has a strong sense of justice and fairness----- Likes to explore new ideas and technologies----- Enjoys learning new things and meeting new people"
person_2_description = (
    "'----1. Personality: Committed to making a positive impact on the world, believes in the power of change through community involvement and political participation.----2. Values: Hard work, education, and community involvement.----3. Background: Born in Honolulu, Hawaii on August 4, 1961, with a Kenyan father and a Kansan mother. 44th President of the United States from 2009 to 2017.----5. Name: Barack Obama----6. Hobbies: Unknown----7. Goals: To bridge divisions and work toward a more inclusive and equitable America.----8. Political Leanings: Democratic'",
)
matching(person_1_description, person_2_description)
