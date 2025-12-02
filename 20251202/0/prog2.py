import asyncio

async def snd():
    evsnd.set()
    print(f"shd: generated {evsnd}")

async def mid(k):
    await evsnd.wait()
    if k:
        
    else:
        pass

    print(f"mid: generated {k}")


async def rcv():
    t1, t2 = "", ""
    await t1.wait()
    print(f"rcv: generated {t1}")
    await t2.wait()
    print(f"rcv: generated {t2}")
    print()