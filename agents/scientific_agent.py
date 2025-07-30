from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from .tools import get_tools

def get_scientific_agent():
    """
    Initializes a conversational agent with access to custom tools.
    """
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    tools = get_tools()
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
