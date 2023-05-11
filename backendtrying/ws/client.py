import asyncio
import websockets

async def main():
    async with websockets.connect("ws://localhost:8765", ping_timeout=None) as websocket:
        while True:
            message = input("Enter a message to send: ")
            await websocket.send(message)

if __name__ == "__main__":
    asyncio.run(main())
