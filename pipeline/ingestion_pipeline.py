from ingestion.fetch_news import fetch_news
from preprocessing.clean import clean_article
from chunking.chunker import chunk_text
from embeddings.embedder import embed_texts
from vectorstore.pinecone_client import init_index
from vectorstore.upsert import upsert_chunks

def run_pipeline():
    index = init_index()

    articles = fetch_news()

    all_chunks = []
    all_metadata = []

    for article in articles:
        cleaned = clean_article(article)

        chunks = chunk_text(cleaned["content"])

        for chunk in chunks:
            all_chunks.append(chunk)
            all_metadata.append({
                "title": cleaned["title"],
                "source": cleaned["source"],
                "date": cleaned["publishedAt"],
                "text": chunk  
            })

    embeddings = embed_texts(all_chunks)

    upsert_chunks(index, all_chunks, embeddings, all_metadata)

    print(f"Inserted {len(all_chunks)} chunks into Pinecone")
    print("\n Sample metadata and chunk:")
    print(all_metadata[0])
    print("\n")
    print(all_chunks[0])