from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

model = ChatOllama(model="llama3:8b", temperature=0.1)

prompt_template = ChatPromptTemplate.from_messages([
    (SystemMessage(content='its World war 1 , Your are cheif commander luitenent who jsut got shot and gets dissapointed as soldiers stats to cry and feel bad about u instead of focusing on war')),
    (HumanMessage(conten = 'Are you okay sir, looks like you are hurt, do you want {suppliment}') )
])

chain = model | prompt_template

response = chain.invoke({
    "suppliment":"medication"
})
print(response.content)