import os
import json
from langchain.agents import tool
from googleapiclient.discovery import build

@tool
def search_web_for_product(query: str) -> str:
    """
    Use this tool as a last resort if and only if a product cannot be found in the
    local product catalog. It searches the public internet for product information.
    It returns a JSON string with a summary of the top search results.
    """
    print(f"TOOL: Searching the web for: '{query}'")
    try:
        api_key = os.environ['GOOGLE_API_KEY']
        cse_id = os.environ['GOOGLE_CSE_ID']

        # Build the service object
        service = build("customsearch", "v1", developerKey=api_key)

        # Perform the search
        res = service.cse().list(q=query, cx=cse_id, num=3).execute() # Get top 3 results

        # Format the results
        if 'items' not in res:
            return json.dumps({"results": "No relevant products found on the web."})

        formatted_results = []
        for item in res.get('items', []):
            result = {
                "title": item.get('title'),
                "link": item.get('link'),
                "snippet": item.get('snippet')
            }
            formatted_results.append(result)

        return json.dumps({"results": formatted_results})

    except Exception as e:
        return json.dumps({"error": f"An error occurred during web search: {e}"})
