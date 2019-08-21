import asyncio
import socket

loop = asyncio.get_event_loop()
rsock, wsock = socket.socketpair()


def reader():
    data = rsock.recv(100)
    print('Received:', data.decode())

    loop.remove_reader(rsock)
    loop.stop()


loop.add_reader(rsock, reader)
loop.call_soon(wsock, 'abc'.encode())

try:
    loop.run_forever()
finally:
    rsock.close()
    wsock.close()
    loop.close()
