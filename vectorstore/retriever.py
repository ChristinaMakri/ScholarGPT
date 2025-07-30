def get_retriever(vectorstore, search_kwargs=None):
    """
    Returns a retriever from the vectorstore with given search parameters.

    Args:
        vectorstore: The vector store instance.
        search_kwargs (dict, optional): Additional search parameters, e.g., {"k": 5}.

    Returns:
        retriever object
    """
    if search_kwargs is None:
        search_kwargs = {"k": 4}
    return vectorstore.as_retriever(search_kwargs=search_kwargs)
