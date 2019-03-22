import asyncio
import websockets

async def message():
        name = input("What's your name? > ")
        while True:
                async with websockets.connect("ws://localhost:1234") as socket:
                        msg = input("Enter message: ")
                        await socket.send(name + ": " + msg)
                        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())

