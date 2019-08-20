import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    addr = writer.get_extra_info('peername')

    print(f'client connected from: {addr}')
    print(f'client sent data: {data.decode()}')
    writer.write(data +  b' REPLY FROM SERVER')
    await writer.drain()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'serving on {addr}...')
    async with server:
        await server.serve_forever()

asyncio.run(main())
