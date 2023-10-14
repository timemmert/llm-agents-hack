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
        # "Hi! My name is Nikhil, and I'm a BS/MS student at Stanford. I'm really passionate about computer vision and animal rights"
        """
I am Barack Obama, and as the 44th President of the United States, I had the incredible privilege of serving this nation from 2009 to 2017. My journey to the White House was a testament to the enduring promise of the American dream.

I was born on August 4, 1961, in Honolulu, Hawaii. My diverse background – a Kenyan father and a Kansan mother – has shaped my perspective and informed my commitment to inclusivity and unity. I often reflect on the values instilled in me by my parents and grandparents, emphasizing hard work, education, and community involvement.

My time as President was marked by several significant achievements. The passage of the Affordable Care Act, also known as Obamacare, expanded access to healthcare for millions of Americans. We took significant steps in addressing climate change through the Paris Agreement and encouraged clean energy innovation. I also sought to strengthen relationships with our international allies and promote diplomacy and multilateral cooperation.

Throughout my tenure, I aimed to bridge divisions and work toward a more inclusive and equitable America. My administration saw the end of the "Don't Ask, Don't Tell" policy, allowing LGBTQ+ individuals to serve openly in the military. We also made strides in criminal justice reform, with the signing of the First Step Act.

The 2008 financial crisis was a significant challenge during my presidency, and my administration worked to stabilize the economy and prevent a further downturn. I aimed to provide economic opportunities for all, believing in the importance of lifting people out of poverty and expanding the middle class.

It was an honor and a privilege to serve as President, and my hope was to inspire young people to engage in civic life, emphasizing the power of change through community involvement and political participation. The road was not always easy, and there were many challenges to overcome, but I remained committed to the belief that, in America, we could achieve greatness through unity, empathy, and hard work.

I continue to be involved in public life, advocating for the values and ideals I hold dear. My time in office may be over, but my commitment to making a positive impact on the world remains steadfast.
"""
    )
)
