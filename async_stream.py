import asyncio
import socket


async def wait_for_data():
    rsock, wsock = socket.socketpair()
    reader, writer = await asyncio.open_connection(sock=rsock)

    loop = asyncio.get_running_loop()
    loop.call_soon(wsock.send, 'abc'.encode())
    data = await reader.read(100)
    print(f'Received data: {data.decode()}')

    print('Closing write socket')
    wsock.close()

    print('Closing writer')
    writer.close()

asyncio.run(wait_for_data())
