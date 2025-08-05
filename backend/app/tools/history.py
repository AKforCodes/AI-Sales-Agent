from langchain.agents import tool
from app.database.queries import log_quote_in_db
import json

@tool
def log_generated_quote(customer_inquiry: str, quote_json_string: str) -> str:
    """
    Use this final tool to log the customer's original inquiry and the final generated quote
    into the order history database. This should be the last step after presenting the quote.
    """
    print("TOOL: Logging quote to DB.")
    try:
        quote_data = json.loads(quote_json_string)
        log_quote_in_db(customer_inquiry, quote_data)
        return "Quote successfully logged to order history."
    except Exception as e:
        return f"Failed to log quote. Error: {e}"
