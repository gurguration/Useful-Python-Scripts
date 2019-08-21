import asyncio
import socket

rsock, wsock = socket.socketpair()
loop = asyncio.get_event_loop()


def reader():
    print('Reading socket')
    data = rsock.recv(100)
    print(f'Received data {data}')
    loop.remove_reader(rsock)
    loop.stop()


loop.add_reader(rsock, reader)
loop.call_soon(wsock.send, 'abc'.encode())

try:
    loop.run_forever()
finally:
    rsock.close()
    wsock.close()
    loop.close()
