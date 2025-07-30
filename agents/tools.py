from langchain.agents import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from asteval import Interpreter

# Δημιουργούμε έναν interpreter once
asteval_interpreter = Interpreter()

def get_tools():
    def calculator_fn(query: str) -> str:
        try:
            result = asteval_interpreter(query)
            return str(result)
        except Exception:
            return "Error in calculation."

    calculator_tool = Tool(
        name="Calculator",
        func=calculator_fn,
        description="Performs basic arithmetic calculations."
    )

    google_search = GoogleSearchAPIWrapper()
    google_tool = Tool(
        name="Google Search",
        func=google_search.run,
        description="Useful for searching the web to answer queries."
    )

    return [calculator_tool, google_tool]
