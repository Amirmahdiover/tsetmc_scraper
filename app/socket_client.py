# app/socket_client.py

# Future Improvement:
# This module is reserved for real-time WebSocket market data streaming.
# It is not used in the current stable API version.

import asyncio
import json
import websockets

TSETMC_SOCKET_URL = "wss://festream.saasexch.cc:8443/nats-fe"

async def tsetmc_stream():
    async with websockets.connect(TSETMC_SOCKET_URL) as ws:
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            yield data

