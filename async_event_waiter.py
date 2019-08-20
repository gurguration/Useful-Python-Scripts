import asyncio

async def waiter(event):
    print('inside waiter will wait for my go')
    await event.wait()
    print('got it!')



async def main():
    event = asyncio.Event()
    task = asyncio.create_task(waiter(event))
    print('starting waiting in main')
    await asyncio.sleep(4)
    event.set()
    await task

asyncio.run(main())
