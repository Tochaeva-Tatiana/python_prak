import random
seq = [(random.random(), bytes(random.sample(range(5),3)), random.randrange(10000)) for i in range(10)]
