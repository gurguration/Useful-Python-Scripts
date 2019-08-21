import asyncio

async def cancel_me():
    print('Cancel me(): before sleep')
    try:
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('Cancel me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    # Create a "cancel_me" Task
    task = create_task(cancel_me())
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('main(): cancel_me is cancelled now')

asyncio.run(main())
