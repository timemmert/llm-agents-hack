from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate


# first initialize the large language model
llm = OpenAI(temperature=0, model_name="text-davinci-003")

# now initialize the conversation chain

prompt_template = PromptTemplate(
    input_variables=["history", "input"],
    template="You are a friendly AI assistant. Your goal is to find out as much \
    as possible about a given person. Try to find out everything about them that \
    their best friend would know: their values, their personality, their \
    hobbies, their background, their age, etc. \
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
#  Given a detailed description of a \
#     person, please write a bulleted \
#     point summary about their personality, their values, their hobbies, and \
#     anything else that another person might be interested in learning about them \
#     in order to become their friend. \
