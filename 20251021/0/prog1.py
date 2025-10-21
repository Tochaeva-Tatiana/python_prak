def filterfalse(seq, n):
    it = iter(seq)
    window = deque(islice(it, n), maxlen=n)
    if not window:
        return