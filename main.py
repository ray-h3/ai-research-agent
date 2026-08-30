import uuid
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from pydantic import BaseModel
from tools import search_tool, wiki_tool, save_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


parser = PydanticOutputParser(
    pydantic_object=ResearchResponse
)


tools = [search_tool, wiki_tool, save_tool]


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant. Use Wikipedia or web search to research the topic. After completing the research, save the final result to a text file using the save_text_to_file tool."
)


query = input("What can I help you research? ")


raw_response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": query
        }
    ]
})


print(raw_response)
