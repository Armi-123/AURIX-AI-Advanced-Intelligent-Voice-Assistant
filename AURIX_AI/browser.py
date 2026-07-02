import webbrowser


# -----------------------------
# OPEN SEARCH
# -----------------------------
def search_web(query):

    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

    return f"Searching Google for {query}"