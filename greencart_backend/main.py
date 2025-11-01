from fastapi import FastAPI, HTTPException
from greencart_backend.agent import GreenCartAgent
from greencart_backend.memory import memory_read, memory_write
from greencart_backend.catalog import search_catalog, get_product, list_products
from pydantic import BaseModel

app = FastAPI()
agent = GreenCartAgent()

class BookingRequest(BaseModel):
    user_id: str
    cart: dict
    shipping: dict
    payment_token: str

@app.post("/search_catalog")
async def api_search_catalog(query: str, top_k: int = 5):
    return search_catalog(query, top_k)

@app.post("/embed_text")
async def api_embed_text(text: str):
    return agent.embed_text(text)

@app.get("/memory_read")
async def api_memory_read(user_id: str, type: str, limit: int = 5):
    return memory_read(user_id, type, limit)

@app.post("/memory_write")
async def api_memory_write(user_id: str, memory_object: dict):
    return memory_write(user_id, memory_object)

@app.post("/create_booking")
async def api_create_booking(req: BookingRequest):
    return agent.create_booking(req.user_id, req.cart, req.shipping, req.payment_token)

@app.get("/get_product")
async def api_get_product(product_id: str):
    return get_product(product_id)

@app.get("/list_products")
async def api_list_products(filters: dict = {}, page: int = 1):
    return list_products(filters, page)

@app.post("/log_interaction")
async def api_log_interaction(metadata: dict):
    agent.log_interaction(metadata)
    return {"ok": True}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return agent.get_metrics()
