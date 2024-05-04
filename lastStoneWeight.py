import heapq
def lastStoneWeight(stones):
    h = [-1 * s for s in stones]
    heapq.heapify(h)

    while len(h) > 1:
        x = heapq.heappop(h)
        y = heapq.heappop(h)
        if x != y:
            heapq.heappush(h, x - y)
    
    return heapq.heappop(h) * -1 if len(h) > 0 else 0

print(lastStoneWeight([2,7,4,1,8,1]))