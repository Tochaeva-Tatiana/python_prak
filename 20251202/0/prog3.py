import asyncio

async def prod(queue, size):
    for i in range(size):
        val = f"value_{i}"
        await queue.put(val)
        await asyncio.sleep()

async def mid(queue, size):
    for i in range(size):
        
