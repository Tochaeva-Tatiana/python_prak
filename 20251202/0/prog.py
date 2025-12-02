import asyncio

async def squarer(n):
    return n**2

async def doubler(n):
    return 2*n

async def main(lst):
    lst2 = await asyncio.gather(squarer(lst[0]), squarer(lst[1]))
    res = await asyncio.gather(doubler(lst2[0]), doubler(lst2[1]))
    print(res)

s = eval(input())
asyncio.run(main(s))