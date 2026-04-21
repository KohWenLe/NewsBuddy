import uuid

def upsert_chunks(index, chunks, embeddings, metadata_list):
    vectors = []

    for i, chunk in enumerate(chunks):
        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embeddings[i].tolist(),
            "metadata": metadata_list[i]
        })

    index.upsert(vectors=vectors)