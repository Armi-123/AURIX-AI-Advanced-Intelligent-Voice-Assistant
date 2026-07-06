import requests



# ==========================================
# WIKIPEDIA SEARCH USING OFFICIAL API
# ==========================================

def search_wiki(query):
    """
    Search Wikipedia using the official REST API.
    """

    query = query.strip()

    if not query:
        return "Please tell me what you want to search."

    try:

        url = (
            f"https://en.wikipedia.org/api/rest_v1/page/summary/"
            f"{query.replace(' ', '_')}"
        )

        headers = {
            "User-Agent": "AURIX-AI/1.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 404:
            return f"Sorry, I couldn't find information about {query}."

        if response.status_code != 200:
            return "Wikipedia service is currently unavailable."

        data = response.json()

        if "extract" in data:
            full_text = data["extract"]

            words = full_text.split()

            short_text = " ".join(words[:30]) + "..."

            return data["extract"]
   
        return "No information available."

    except requests.exceptions.ConnectionError:
        return "No internet connection."

    except requests.exceptions.Timeout:
        return "Wikipedia request timed out."

    except Exception as e:
        return f"Wikipedia Error: {e}"