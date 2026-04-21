def clean_article(article):
    return {
        "title": article.get("title", ""),
        "content": article.get("content") or article.get("description", ""),
        "source": article["source"]["name"],
        "publishedAt": article.get("publishedAt")
    }