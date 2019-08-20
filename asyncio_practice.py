import asyncio
import time
import random

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     print(f'starting async main at {time.strftime("%X")}')
#     await say_after(10, 'hello')
#     # await say_after(random.randrange(1,5), 'hello')
#     # await say_after(random.randrange(1,5), 'world')
#     await say_after(4, 'world')

    
# asyncio.run(main())

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(f'Hello {what}')

# async def main():
#     print(f'Entered main at {time.strftime("%X")}')
#     task1 = asyncio.create_task(say_after(random.randrange(1,5), 'hello'))
#     task2 = asyncio.create_task(say_after(random.randrange(1,5), 'world'))
#     await task1
#     await task2
#     print(f'Finished at {time.strftime("%X")}')

# asyncio.run(main())

# async def nested():
#     print(42)
#     return 42


# async def main():
#     task = asyncio.create_task(nested())
#     await task


# asyncio.run(main())

# import datetime

# async def current_time():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5
#     while True:
#         print(f'current time is {datetime.datetime.now()}')
#         await asyncio.sleep(1)
#         if loop.time() >= end_time:
#             break

# asyncio.run(current_time())


# async def factiorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f'Computing factorial {name}: for {i}')
#         f *= i
#         await asyncio.sleep(1)
#     print(f'Task {name}: factorial({number}) = {f}')

# async def main():
#     await asyncio.gather(
#         factiorial('A', 3),
#         factiorial('B', 5),
#         factiorial('C', 9),
#     )
# asyncio.run(main())


# async def eternity():
#     await asyncio.sleep(3)
#     print('YAY!')

# async def main():
#     try:
#         coro = asyncio.create_task(eternity())
#         done, pending = await asyncio.wait({coro})
#         print(done, 'done?')
#         print(pending, 'pending?')
#     except asyncio.TimeoutError as e:
#         print('timeout')


# asyncio.run(main())
