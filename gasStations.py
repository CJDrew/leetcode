def canCompleteCircuit(gas, cost) -> int:
    #Observation: if you can't make it from a -> b, no need to check any point inbetween
    i = 0
    while i < len(gas):
        #Rearrange the lists so our starting point is always in the front
        tGas, tCost = gas[i:] + gas[:i], cost[i:] + cost[:i]
        curGas = tGas[i]
        curIndex = 0
        #Keep visiting as many as we can
        while curGas >= tCost[curIndex]:
            #If we made it to the end then we did it
            if curIndex == len(tGas) - 1:
                return i
            curGas -= tCost[curIndex]
            curIndex += 1
            curGas += tGas[curIndex]
        #If we failed, skip ahead. Not sure if max is needed but I don't want to get stuck
        i += max(curIndex, 1)
    return -1

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))