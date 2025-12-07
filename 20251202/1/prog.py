import asyncio


async def writer(queue, delay, stop_event):
    await asyncio.sleep(delay)
    i = 0
    while not stop_event.is_set():
        value = f"{i}_{delay}"
        await queue.put(value)
        i += 1
        await asyncio.sleep(delay)


async def stacker(queue, stack, stop_event):
    while True:
        if stop_event.is_set() and queue.empty():
            return
        try:
            value = await asyncio.wait_for(queue.get(), timeout=0.1)
            stack.append(value)
        except asyncio.TimeoutError:
            pass




async def reader(stack, count, delay, stop_event):
    await asyncio.sleep(delay)
    for _ in range(count):
        while not stack:
            await asyncio.sleep(0)
        value = stack.pop()
        print(value)
        await asyncio.sleep(delay)
    stop_event.set()


async def main():
    d1, d2, d3, cnt = map(int, input().split(","))

    q = asyncio.Queue()
    stack = []
    stop_event = asyncio.Event()

    tasks = [
        asyncio.create_task(writer(q, d1, stop_event)),
        asyncio.create_task(writer(q, d2, stop_event)),
        asyncio.create_task(stacker(q, stack, stop_event)),
        asyncio.create_task(reader(stack, cnt, d3, stop_event)),
    ]

    await asyncio.gather(*tasks, return_exceptions=True)


asyncio.run(main())
