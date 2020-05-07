import math
import random

def slowfun():
    cache = {}
    def fasterfun(x, y):
        # TODO: Modify to produce the same results, but much faster
        if str(x + y) not in cache:
            v  = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            cache[str(x + y)] = v

        return cache[str(x + y)] 
    
    return fasterfun


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    fasterfun = slowfun()

    print(f'{i}: {x},{y}: {fasterfun(x, y)}')
