from langchain.chat_models import ChatOpenAI
from dotenv import dotenv_values
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory


OPENAI_API_KEY = dotenv_values(".env") 

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY,temperature=0.5)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}")
])

memory = ConversationBufferMemory(return_messages=True,memory_key="chat_history")

chain = prompt | model