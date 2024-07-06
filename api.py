from typing import Annotated
from pydantic import BaseModel, Field

from fastapi import FastAPI, Body
from mangum import Mangum
import uvicorn
from scripts.chat import Chatbot

app = FastAPI()
handler=Mangum(app)


class Prompt(BaseModel):
    prompt: str | None = Field(default=None, title="Prompt system")
    user_message: str = Field(default=None,title="user message")


@app.post("/session/{chat_session}")
async def chat(chat_session: str, prompt: Annotated[Prompt, Body(embed=True)]):
    chat = Chatbot(system_message=prompt.prompt,session_id=chat_session)
    response = chat.send_message(query=prompt.user_message)
    results = {"Ai_response": response.content, "ChatId": response.id}
    return results

@app.get('/session/{chat_session}/history')
def chat_history(chat_session:str):
   history = Chatbot(session_id=chat_session).history
   return {'chat_session':chat_session,"history":history}

if __name__=="__main__":
  uvicorn.run(app,host="0.0.0.0",port=9000)