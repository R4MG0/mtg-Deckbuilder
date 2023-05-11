import asyncio
import websockets
import threading

name = ""
async def hello():
    async with websockets.connect("ws://localhost:8765", ping_timeout=None) as ws:
        while True:
            print(await ws.recv())
            # name = 'a'
            # if(name != ""):
            #     # await ws.send("name")
            #     test = await ws.recv()
            #     print(test)
            #     # print(f"sent: {name}")
            #     name = ""


        # greeting = await websocket.recv()
        # print(f"< {greeting}")

# async def ui():
#     global name = input("Write sth: ")

if __name__ == '__main__':
    asyncio.run(hello())
