# backend/search.py

from exa_py import Exa
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get your key from the environment
EXA_API_KEY = os.getenv("EXA_API_KEY")
exa = Exa(EXA_API_KEY)

def search_exa(query: str, domains: list = None, num_results: int = 5):
    if not query:
        return []

    try:
        results = exa.search(
            query,
            num_results=num_results,
            type='keyword',
            include_domains=domains or [],
        )

        return [
            {"title": r.title, "url": r.url}
            for r in results.results
        ]

    except Exception as e:
        print("Exa API error:", e)
        return []

