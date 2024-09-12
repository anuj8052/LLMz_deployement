from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
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

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI()
prompt1 = ChatPromptTemplate.from_template("Provide me an essay about {topic}")
prompt2 = ChatPromptTemplate.from_template("provide me the summary of an essay about {}")
prompt3 = ChatPromptTemplate.from_template("Describe the papularity of a {celebrity} in india")

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | model,
    path="/summary"
)

add_routes(
    app,
    prompt3 | model,
    path="/celebrity"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)