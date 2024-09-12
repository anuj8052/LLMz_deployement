from fastapi import FastAPI, Request
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
import uvicorn
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    print("OPENAI_API_KEY environment variable is not set. Please set it in your .env file.")
    exit(1)

app = FastAPI(
    title="Langchain server",
    version=1.0,
    description="A simple API server"
)

model = ChatOpenAI()
prompt1 = ChatPromptTemplate.from_template("Provide me an essay about {topic}")
prompt2 = ChatPromptTemplate.from_template("provide me the summary of an essay about {}")
prompt3 = ChatPromptTemplate.from_template("Describe the papularity of a {celebrity} in india")

@app.post("/openai")
async def openai(request: Request):
    # You'll need to implement the logic for this endpoint
    return {"response": "OpenAI endpoint"}

@app.post("/essay")
async def essay(request: Request):
    topic = (await request.json())["topic"]
    response = model.generate_text(prompt1.format(topic=topic))
    return {"response": response}

@app.post("/summary")
async def summary(request: Request):
    topic = (await request.json())["topic"]
    response = model.generate_text(prompt2.format(topic=topic))
    return {"response": response}

@app.post("/celebrity")
async def celebrity(request: Request):
    celebrity = (await request.json())["celebrity"]
    response = model.generate_text(prompt3.format(celebrity=celebrity))
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)