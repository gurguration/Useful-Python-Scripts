import asyncio
import socket


class MyProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.transport = None
        self.on_con_lost = loop.create_future()

    def connection_made(self, transport):
        print('made connection')
        # print(transport)
        self.transport = transport

    def connection_lost(self, exc):
        print('connection lost goodbye')
        self.on_con_lost.set_result(True)

    def data_received(self, data):
        print('Received: ', data.decode())
        self.transport.close()


async def main():
    loop = asyncio.get_running_loop()

    rsock, wsock = socket.socketpair()

    transport, protocol = await loop.create_connection(lambda: MyProtocol(loop), sock=rsock)
    loop.call_soon(wsock.send, 'abc'.encode())

    try:
        await protocol.on_con_lost
    finally:
        transport.close()
        wsock.close()

asyncio.run(main())
