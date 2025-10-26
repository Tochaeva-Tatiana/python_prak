print(*sorted(filter(lambda s: s.count("TOR") == 2, map("".join, __import__("itertools").product("TOR", repeat=int(input()))))), sep=", ")
