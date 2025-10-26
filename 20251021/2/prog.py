from itertools import islice
from collections import deque

def slide(seq, n):
    it = iter(seq)
    window = deque(islice(it, n), maxlen=n)
    if not window:
        return

    while True:
        yield from window
        try:
            window.append(next(it))
        except StopIteration:
            window.popleft()
            while window:
                yield from window
                window.popleft()
            return


import sys
exec(sys.stdin.read())