import asyncio
from urllib import parse
import sys

async def print_http_headers(url):
    url = parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(url.hostname, 80)

    # query = (
    #     f'HEAD {url.path or "/"} HTTP/1.1\r\n'
    #     f'Host: {url.hostname}\r\n'
    #     f'\r\n'
    # )
    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )
    writer.write(query.encode())
    while True:
        data = await reader.readline()
        if not data:
            break
        data = data.decode().rstrip()
        if data:
            print(f'HTTP header> {data}')
        writer.close()  


url = sys.argv[1]

asyncio.run(print_http_headers(url))
