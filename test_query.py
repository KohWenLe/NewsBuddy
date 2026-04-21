from pipeline.query_pipeline import run_query

query = "latest AI breakthroughs"

results = run_query(query)

for r in results:
    print("=" * 50)
    print("Score:", r["score"])
    print("Title:", r["title"])
    print("Source:", r["source"])
    print("Date:", r["date"])
    print("Text:", r["text"][:200])