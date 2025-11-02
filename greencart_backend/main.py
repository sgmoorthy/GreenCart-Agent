from fastapi import FastAPI, Request
from greencart_backend.agent import GreenCartAgent
from greencart_backend.catalog import search_catalog, get_product, list_products
from greencart_backend.memory import memory_read, memory_write

app = FastAPI()
agent = GreenCartAgent()

@app.get("/search")
async def api_search_catalog(q: str):
    return search_catalog(q)

@app.get("/products")
async def api_list_products():
    return list_products()

@app.get("/product/{product_id}")
async def api_get_product(product_id: str):
    return get_product(product_id)

@app.post("/memory/read")
async def api_memory_read(request: Request):
    body = await request.json()
    return memory_read(body.get("user_id"))

@app.post("/memory/write")
async def api_memory_write(request: Request):
    body = await request.json()
    return memory_write(body.get("user_id"), body.get("data"))

@app.post("/booking")
async def api_create_booking(request: Request):
    data = await request.json()
    return agent.create_booking(data)

@app.post("/log")
async def api_log_interaction(request: Request):
    data = await request.json()
    return agent.log_interaction(data)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/metrics")
async def metrics():
    return agent.get_metrics()
