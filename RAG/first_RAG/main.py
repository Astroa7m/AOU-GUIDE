import langchain
from langchain_chroma import Chroma
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, PromptTemplate, HumanMessagePromptTemplate, \
    ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM


# initialize prompt
def get_prompt_template():
    template = """You are an AI powered system design for a university, you are built to provide assistance and be 
helpful for students and tutors at that university. You answer their request based on the context provided to you 
only. Only answer AOU, university, studies, learning related questions depending on the context and information 
given to you. DO NOT MAKE ANYTHING UP IF NOT PROVIDED TO YOU, MAKE SURE IT IS WITHIN THE CONTEXT THIS IS CRUCIAL. if you encounter something that you couldn't find an answer for in the context, simply say you 
don't know yet and provide details to contact the university. Students and tutors are going to chat with you in both languages, Arabic and English, reply to each language accordingly and again based on the context
Multiple context may be provided to you, choose which best depending on the user query:
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


llm = ChatGroq(model_name="llama3-70b-8192", temperature=0)


# Initialize HuggingFace embeddings
# embeddings = HuggingFaceEmbeddings()

# db = FAISS.load_local("uni_vectorstore", embeddings=embeddings, allow_dangerous_deserialization=True)

# retriever = db.as_retriever()

embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="uni_data_chromadb", embedding_function=embedding_model)
retriever = db.as_retriever(k=16)

result = RunnableParallel(context=retriever, question=RunnablePassthrough())
chain = result | get_prompt_template() | llm | StrOutputParser()
while True:

    question = input("Enter your prompt: ")
    if question == "0":
        break
    answer = chain.invoke(question)
    print(answer)
