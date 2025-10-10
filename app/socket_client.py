# # app/socket_client.py
# import asyncio
# import json
# import websockets

# TSETMC_SOCKET_URL = "wss://stream.tsetmc.com/socket"  # Example, you’ll find the real one

# async def tsetmc_stream(ins_code: str):
#     async with websockets.connect(TSETMC_SOCKET_URL) as ws:
#         # Subscribe to a specific symbol
#         sub_msg = {"type": "subscribe", "insCode": ins_code}
#         await ws.send(json.dumps(sub_msg))

#         while True:
#             msg = await ws.recv()
#             data = json.loads(msg)
#             yield data  # Stream each message as it arrives
import asyncio
import random

async def tsetmc_stream(ins_code: str):
    while True:
        await asyncio.sleep(2)  # simulate delay between updates
        yield {
            "insCode": ins_code,
            "price": round(random.uniform(100, 500), 2),
            "volume": random.randint(1000, 10000)
        }
