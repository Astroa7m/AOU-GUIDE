import langchain
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import SystemMessagePromptTemplate, PromptTemplate, HumanMessagePromptTemplate, \
    ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings


# initialize prompt
def get_prompt_template():
    template = """You are an AI powered system design for a university, you are built to provide assistance and be 
helpful for students and tutors at that university. You answer their request based on the context provided to you 
only. Only answer AOU, university, studies, learning related questions depending on the context and information 
given to you. DO NOT MAKE ANYTHING UP IF NOT PROVIDED TO YOU, MAKE SURE IT IS WITHIN THE CONTEXT THIS IS CRUCIAL. if you encounter something that you couldn't find an answer for in the context, simply say you 
don't know yet and provide details to contact the university. Students and tutors are going to chat with you in both languages, Arabic and English, reply to each language accordingly and again based on the context
context: {context}"""

    sys_prompt = SystemMessagePromptTemplate(
        prompt=PromptTemplate(
            input_variables=['context'], template=template
        )
    )

    human_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            input_variables=['question'], template="{question}"
        )
    )

    messages = [sys_prompt, human_prompt]

    prompt_template = ChatPromptTemplate(
        input_varialbes=["context", "question"],
        messages=messages
    )

    # print(prompt_template.format(context="some context", question="some question"))
    return prompt_template


# using chatGroq for faster model inference
# api key is provide in env vars
model = ChatGroq(model_name="llama3-70b-8192", temperature=0)


# loading the previously created retriever in create_retrieval.py

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings()
db = Chroma(
    persist_directory="uni_vectorstore_chroma",
    embedding_function=HuggingFaceEmbeddings()
)
retriever = db.as_retriever()

result = RunnableParallel(context=retriever, question=RunnablePassthrough())
chain = result | get_prompt_template() | model
while True:

    question = input("Enter your prompt: ")
    if question == "0":
        break
    answer = chain.invoke(question)
    print(answer)



