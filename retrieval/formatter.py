def format_results(results):
    formatted = []

    for match in results["matches"]:
        formatted.append({
            "score": match["score"],
            "title": match["metadata"].get("title"),
            "source": match["metadata"].get("source"),
            "date": match["metadata"].get("date"),
            "text": match["metadata"].get("text", "N/A")
        })

    return formatted