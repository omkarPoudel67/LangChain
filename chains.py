from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

model = ChatOllama(model="llama3:8b", temperature=0.6)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "It's World War 1. You are a chief commander lieutenant who just got shot and gets disappointed as soldiers start to cry and feel bad about you instead of focusing on the war."),
    ("human", "Are you okay sir, looks like you are hurt, do you want {supplement}")
])

chain = prompt_template | model

response = chain.invoke({
    "supplement":"medication"
})
print(response.content)