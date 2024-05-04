from collections import defaultdict
def checkInclusion(s1: str, s2: str):
    if len(s1) > len(s2):
        return False

    targetDic = defaultdict(int)
    for letter in s1:
        targetDic[letter] += 1
    
    curDic = defaultdict(int)
    for letter in s2[:len(s1)]:
        curDic[letter] += 1
    
    if curDic == targetDic:
        return True

    for i in range(len(s1), len(s2)):
        curDic[s2[i - len(s1)]] -= 1
        curDic[s2[i]] += 1
        if curDic == targetDic:
            return True
    
    return False

print(checkInclusion("ab", "eidbaooo"))