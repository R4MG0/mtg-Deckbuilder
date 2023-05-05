import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    # await websocket.send(greeting)
    # print(f"> {greeting}")

async def start_server():
    async with websockets.serve(countPlayers, "localhost", 2319):
        await asyncio.Future()  # run forever

n = 1
async def countPlayers(ws, path):
    
    start = False
    while not start:
        try:
            tmp = await ws.recv()
            if(not tmp.__contains__("WebSocketCommonProtocol")):
                print(tmp)
                if(str(tmp) == "start"):
                    print(f'{n} Players connected')
                    start = True
                    break
                    break
                    break
                    # return n
                    
                else:print("incr");n = n + 1
        except:
            nothing()
    print(n)

def nothing():
    return

tmpstorage = ''
async def handleTurns(ws, path):
    get = ws.recv()
    for i in range():
        ws.send(get)

if __name__ == '__main__':
    asyncio.run(start_server())
