import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print(f'Send message: {message}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'received data: {data.decode()}')
    
    print(f'close the connection')
    writer.close()

    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World'))
