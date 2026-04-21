from embeddings.embedder import embed_query

def semantic_search(index, query, top_k=5):
    query_vector = embed_query(query)

    results = index.query(
        vector=query_vector.tolist(),
        top_k=top_k,
        include_metadata=True
    )

    return results