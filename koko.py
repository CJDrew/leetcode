piles = [3,6,7,11]
h = 8

def canEat(k):
    total = 0
    for p in piles:
        total += (p // k) + (1 if p % k != 0 else 0)
    return total <= h

print(canEat(4))