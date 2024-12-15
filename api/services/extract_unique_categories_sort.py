from typing import List, Dict

async def extract_unique_categories(items: List[Dict]) -> List[str]:
    """Extract unique categories from a list of DynamoDB items."""
    categories = {item["category"]["S"] for item in items if "category" in item}
    return list(categories)