from groq import Groq
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model= ChatGroq(api_key = os.getenv("API_KEY"),
                model = "llama-3.3-70b-versatile",
                temperature = 1
                )



# client = Groq(api_key = os.getenv('API_KEY'))

# models = client.models.list()

# for model in models.data:
#     print(f"id:{model.id}\n owned_by: {model.owned_by},\n context_window: {model.context_window}\n\n")



conversation =[
    {"role":"system", "content":"the user you are speaking to right now is Omkar"},
    {"role":"user", "content":"hey whats my name , and also say abnout nepal in 50 words"}
]

chunks = model.stream(conversation)
for chunk in chunks:
    print(chunk.content)

