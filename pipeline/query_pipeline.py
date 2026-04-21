from vectorstore.pinecone_client import init_index
from retrieval.semantic_search import semantic_search
from retrieval.formatter import format_results

def run_query(query):
    index = init_index()

    results = semantic_search(index, query)
    formatted = format_results(results)

    return formatted