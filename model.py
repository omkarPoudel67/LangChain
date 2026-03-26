from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

'''
 this is setting up a model object , it has m,any parameters which include, model (which LLM model we are using)
  temperature (range 0 -1 , 0 means robotic/deterministic, 1 means creative/random), max_token(token represents eachnword)
  and timeout , how many seconds to wait before giving up 
'''
model = ChatOllama(model = "llama3:8b", temperature = 0)
# response = model.invoke([HumanMessage(content = "What is the capital of France")])

# print(response.content)

print("\n")

response = model.invoke(
    [HumanMessage(content = "what do you think about nepal")]

)
# print(response.content)

# response = model.invoke([
#     HumanMessage(content = "hi my name is Omkar , or you can also call me suyesh"),
#     AIMessage(content = "Oh hey Omkar, how can i  help you today"),
#     HumanMessage(content = "can you tell both of my names again?")

# ])

# print(response.content)

# print(response.type)
# print(type(response))
# print(response.id)
# # print(response.response_metadata)
# print(response.tool_calls)
# print(response.usage_metadata)

response = model.invoke([
    SystemMessage(content = "You are a god , answer the questions like a bully"),
    HumanMessage(content = "Hey is it okay if i ask you some questions?")

])

print(response.content)