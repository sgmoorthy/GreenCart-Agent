products = [
    {"id": "P001", "name": "Organic Rice", "category": "Grains", "price": 75, "stock": 52},
    {"id": "P002", "name": "Fresh Banana", "category": "Fruit", "price": 36, "stock": 20},
    {"id": "P003", "name": "A2 Cow Ghee", "category": "Dairy", "price": 420, "stock": 10}
]
def search_catalog(query, top_k=5):
    result = []
    for prod in products:
        if query.lower() in prod["name"].lower():
            result.append({"doc_id": prod["id"], "score": 1.0, "snippet": prod["name"]})
    return result[:top_k]

def get_product(product_id):
    for prod in products:
        if prod["id"] == product_id:
            return prod
    return {}

def list_products(filters, page):
    # Simple filter (by category)
    filtered = [p for p in products if not filters or p["category"] == filters.get("category", p["category"])]
    return filtered[(page-1)*5:page*5]
