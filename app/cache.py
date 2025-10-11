import redis
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()
# Connect to local Redis server
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# TTL for caching (e.g. 2 minutes)
CACHE_TTL = 120

def get_cached_data(key: str):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None

def set_cached_data(key: str, value, ttl=CACHE_TTL):
    json_data = json.dumps(value)
    r.setex(key, ttl, json_data)
