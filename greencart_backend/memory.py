from collections import defaultdict
import time

_memory = defaultdict(list)

def memory_read(user_id, type, limit=5):
    return list(filter(lambda m: m.get("type") == type, _memory[user_id]))[-limit:]

def memory_write(user_id, memory_object):
    memory_object["created"] = time.time()
    _memory[user_id].append(memory_object)
    return {"ok": True}
