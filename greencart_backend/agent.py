from .catalog import search_catalog
from .memory import memory_write
import uuid
import time

class GreenCartAgent:
    def __init__(self):
        self.bookings = []
        self.logs = []
    
    def create_booking(self, data):
        order = {"order_id": len(self.bookings) + 1, "details": data, "status": "confirmed"}
        self.bookings.append(order)
        return order

    def embed_text(self, text):
        # Dummy embedding logic
        return hash(text)

    def log_interaction(self, data):
        self.logs.append(data)
        return {"logged": True}

    def get_metrics(self):
        return {
            "total_bookings": len(self.bookings),
            "total_logs": len(self.logs)
        }
