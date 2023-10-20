import heapq
from collections import deque, Counter

def leastInterval(tasks, n):
    counts = Counter(tasks)
    maxHeap = [-c for c in counts.values()]
    heapq.heapify(maxHeap)

    cooldowns = deque()
    timer = 0

    while maxHeap or cooldowns:
        #Check for an action that's at cooldown
        if cooldowns and cooldowns[0][1] < timer:
            heapq.heappush(maxHeap, cooldowns.popleft()[0])
        if maxHeap:
            cur = heapq.heappop(maxHeap)
            cur += 1
            if cur < 0:
                cooldowns.append((cur, timer + n))
        timer += 1
    
    return timer

leastInterval(["A","A","A","B","B","B"], 2)