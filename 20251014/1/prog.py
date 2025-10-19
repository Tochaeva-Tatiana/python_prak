s = input()

pairs = set()
prev = None

for ch in s:
    if ch.isalpha():
        ch_low = ch.lower()
        if prev is not None:
            pairs.add(prev + ch_low)
        prev = ch_low
    else:
        prev = None

print(len(pairs))
