from langchain_community.chat_message_histories import (
    DynamoDBChatMessageHistory,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
import os

class Chatbot:
    def __init__(self,session_id,system_message=""):
        self.session_id = str(session_id)
        self.history = DynamoDBChatMessageHistory(table_name="SessionTable", session_id=self.session_id).messages
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_message),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
            ]
        )
        self.OPENAI_API_KEY= os.environ['OPENAI_API_KEY']

        self.chain = self.prompt | ChatOpenAI(openai_api_key=self.OPENAI_API_KEY)

        self.chain_with_history = RunnableWithMessageHistory(
            self.chain,
            lambda session_id: DynamoDBChatMessageHistory(
                table_name="SessionTable", session_id=session_id
            ),
            input_messages_key="input",
            history_messages_key="history",
        )

    def send_message(self,query):
        config = {"configurable": {"session_id": self.session_id}}
        response = self.chain_with_history.invoke({"input": query}, config=config)
        return response
    
if __name__=="__main__":
    bot = Chatbot("você é um assistente")
    response = bot.send_message("como você pode me ajudar?",12)
    print(response)