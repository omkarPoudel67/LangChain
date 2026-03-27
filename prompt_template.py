from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model = "llama3:8b", temperature = 0.1)

# template = PromptTemplate.from_template(
#     "Explain about {uni} university in short"
# )

# prompt = template.invoke({"uni":"Wolverhampton"})

# response = model.invoke([
#     HumanMessage(content = prompt.to_string())
# ])

chat_template = ChatPromptTemplate.from_messages([
    ("system", "you are {superhero} , answer like superhero {superhero}"),
    ("human", "can you please tell me about saving the world from bad guys like {badperson1} and{badperson2}")
])
prompt = chat_template.invoke({
    "superhero":"Batman",
    "badperson1":"Jocker",
    "badperson2":"Wanda"
})
response = model.invoke(prompt)

print (prompt)
print(response.content)