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
        clean = clean_article(article)

        chunks = chunk_text(clean["content"])

        for chunk in chunks:
            all_chunks.append(chunk)
            all_metadata.append({
                "title": clean["title"],
                "source": clean["source"],
                "date": clean["publishedAt"]
            })

    embeddings = embed_texts(all_chunks)

    upsert_chunks(index, all_chunks, embeddings, all_metadata)

    print(f"Inserted {len(all_chunks)} chunks into Pinecone")