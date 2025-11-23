import sys



broken_text = sys.stdin.read()


fixed_text = (
    broken_text
    .encode("latin1", errors="replace")
    .decode("cp1251", errors="replace")
)

sys.stdout.write(fixed_text)


