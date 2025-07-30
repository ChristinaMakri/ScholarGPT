from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI

def get_summary_memory():
    """
    Creates and returns a ConversationSummaryMemory instance
    that summarizes conversation context to manage token limits.
    """
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    memory = ConversationSummaryMemory(
        llm=llm,
        memory_key="chat_history",
        return_messages=True
    )
    return memory
