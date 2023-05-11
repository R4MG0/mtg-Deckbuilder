import asyncio
import websockets

# Set of all connected clients
connected = set()

async def handler(websocket, path):
    # Add client to the set of connected clients
    connected.add(websocket)
    try:
        async for message in websocket:
            # Broadcast message to all connected clients
            for client in connected:
                await client.send(message)
    finally:
        # Remove client from the set of connected clients
        connected.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765, ping_timeout=None):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
