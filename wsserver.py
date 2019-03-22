import asyncio
import websockets

async def response(websockets, path):
    message = await websockets.recv()
    print(message)
    await websockets.send(message)

start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
