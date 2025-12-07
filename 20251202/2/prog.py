import asyncio
import random


async def merge(A1, A2, start, middle, finish,
                ev_in1, ev_in2, ev_out):
    await ev_in1.wait()
    await ev_in2.wait()

    i, j, k = start, middle, start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1

    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    ev_out.set()


async def mtasks(A):
    n = len(A)

    src = A[:]              # A не портим
    dst = [None] * n

    tasks = []

    # события: "отрезок, начинающийся здесь, отсортирован"
    events = {i: asyncio.Event() for i in range(n)}
    for ev in events.values():
        ev.set()

    size = 1
    write_to_dst = True

    while size < n:
        new_events = {}

        for start in range(0, n, 2 * size):
            mid = min(start + size, n)
            fin = min(start + 2 * size, n)

            ev1 = events[start]
            ev2 = events[mid] if mid < n else asyncio.Event()
            ev2.set()

            ev_out = asyncio.Event()
            new_events[start] = ev_out

            if write_to_dst:
                tasks.append(
                    asyncio.create_task(
                        merge(src, dst, start, mid, fin, ev1, ev2, ev_out)
                    )
                )
            else:
                tasks.append(
                    asyncio.create_task(
                        merge(dst, src, start, mid, fin, ev1, ev2, ev_out)
                    )
                )

        events = new_events
        size *= 2
        write_to_dst = not write_to_dst

    if not write_to_dst:
        dst[:] = src[:]

    return tasks, dst




import sys
exec(sys.stdin.read())
