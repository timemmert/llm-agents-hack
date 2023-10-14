from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate


# first initialize the large language model
llm = OpenAI(temperature=0, model_name="text-davinci-003")

# now initialize the conversation chain

prompt_template = PromptTemplate(
    input_variables=["history", "input"],
    template="Given a detailed description of a \
    person, please write a bulleted \
    point summary about \
    1. Their personality\
    2. Their values \
    3. Their background (educational, where they grew up, etc.) \
    4. Their age \
    5. Their name \
    6. Their hobbies \
    7. Their goals \
    8. Their political leanings. \
    Format this like    \
    1. Personality\
    2. Values \
    3. ...\
    Do not hallucinate facts. If you do not know something about the user (e.g., \
    their age), make an educated guess but don't hallucinate. \
    Current conversation: {history} \
    Human: {input} \
    AI:",
)
conversation_buf = ConversationChain(
    llm=llm, memory=ConversationBufferMemory(), prompt=prompt_template
)
print(
    conversation_buf(
        "Hi! My name is Nikhil, and I'm a BS/MS student at Stanford. I'm really passionate about computer vision and animal rights"
    )
)
