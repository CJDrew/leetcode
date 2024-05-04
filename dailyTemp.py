def dailyTemperatures(temperatures):
    ans = [0 for i in range(len(temperatures))]
    stack = []

    for i in range(len(temperatures)):
        while len(stack) > 0 and temperatures[i] > stack[-1][0]:
            cur = stack.pop()
            ans[cur[1]] = i - cur[1]
        stack.append((temperatures[i], i))

    return ans

dailyTemperatures([73,74,75,71,69,72,76,73])