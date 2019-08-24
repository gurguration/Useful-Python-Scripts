
import asyncio
import time 

async def waiter():
    print('hello from infinite sleeper')
    await asyncio.sleep(5000)
    print('waiting on infinity')

async def second_waiter():
    print('hello from second waiter')
    print('waiting to raise exception in 3 seconds...\n')
    await asyncio.sleep(3)
    raise
    print("this shouldn't print")

  
async def third_waiter():
    sleep_time = 2
    print(f"third waiter: sleeping for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f'third after {sleep_time} second sleep')


async def main():
    stime = time.time()
    newline = '\n\n\n'
    done,  pending = await asyncio.wait(
        {
            waiter(), 
            second_waiter(), 
            third_waiter()}, 
        timeout=10,
        # return_when="ALL_COMPLETED")
        # return_when="FIRST_COMPLETED")
        return_when="FIRST_EXCEPTION")
    print(f"{newline[:2]}Done tasks[{len(done)}]: {done}\n\n Pending tasks[{len(pending)}]: { newline.join([str(x) for x in list(pending)])}")
    print(f'main finished in: {stime - time.time()}')


asyncio.run(main())
