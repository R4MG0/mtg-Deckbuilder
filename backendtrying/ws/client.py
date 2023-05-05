import asyncio
import websockets
import threading

name = ""
async def hello():
    async with websockets.connect("ws://localhost:2319") as ws:
        # name = input("")
        name = 'a'
        if(name != ""):
            await ws.send("name")
            await ws.send("start")
            # print(f"sent: {name}")
            name = ""


        # greeting = await websocket.recv()
        # print(f"< {greeting}")

# async def ui():
#     global name = input("Write sth: ")

if __name__ == '__main__':
    asyncio.run(hello())
