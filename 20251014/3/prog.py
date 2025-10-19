from collections import Counter

W = int(input())

lines = []
while True:
    line = input()

    if line == '':
        break
    lines.append(line)

text = '\n'.join(lines)

clean_chars = []
for ch in text:
    if ch.isalpha():
        clean_chars.append(ch.lower())
    else:
        clean_chars.append(' ')
clean_text = ''.join(clean_chars)

words = clean_text.split()

cnt = Counter(w for w in words if len(w) == W)

if cnt:
    max_freq = max(cnt.values())
    most_popular = sorted(w for w, c in cnt.items() if c == max_freq)
    print(' '.join(most_popular))
