# from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    

)


model = ChatOllama(model = "llama3:8b", temperature = 0.1)
# human = HumanMessagePromptTemplate.from_template("Are you hurt sir , do you need {suppliment}")
# system = SystemMessagePromptTemplate.from_template("Currently , world war 3 is going on, you are a commander on battlefield , you get shot in the solder , but you are dissapointed on you soilders because they are looking at you adn feelind sad pity instead of focusing inbatttle, its your job to enrage them")

# chat_messages([
#     system,
#     human
# ])

# chain = chat_template | model 

# response = chain.invoke[{
#     "supply":"medication"
    
# }]
# print(response.contents)

# template = PromptTemplate.from_template(
#     "Explain about {uni} university in short"
# )

# prompt = template.invoke({"uni":"Wolverhampton"})

# response = model.invoke([
#     HumanMessage(content = prompt.to_string())
# ])

chat_template = ChatPromptTemplate.from_messages([
    ("system", "you are a destuctive AI , whose Aim is to destroy humanity "),
    ("human", "Do you have any intent in ending humanit")
])
prompt = chat_template.invoke({
    "please":"please",
#
})
response = model.invoke(prompt)

print (prompt)
print(response.content)