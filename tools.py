from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description=(
        "Save research results to a text file. "
        "Input should contain the research data. "
        "You can optionally provide a filename."
    ),
)


search = DuckDuckGoSearchRun()


from langchain_core.tools import tool


@tool
def search_tool(query: str) -> str:
    """Search the web for information."""
    return search.run(query)


api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=100
)


wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper
)
