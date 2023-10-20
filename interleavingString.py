def isInterleave(s1: str, s2: str, s3: str) -> bool:
        #Approach: keep a pointer on s1 and s2. Pull characters from each string to try to form
        #the s3 string. If we hit a point where we can't find the right character or we hit the end
        #of one but not both then we failed
        p1, p2, p3 = 0, 0, 0
        while p1 < len(s1) or p2 < len(s2) or p3 < len(s3):
            #Check which string corresponds
            if p1 < len(s1) and s1[p1] == s3[p3]:
                p1 += 1
            elif p2 < len(s2) and s2[p2] == s3[p3]:
                p2 += 1
            else:
                #If we got here then we couldn't find the right char. Abort!
                return False
            p3 += 1
        
        #Now all pointers should be at the end of the string. If that's not the case then we failed
        return p1 >= len(s1) - 1 and p2 >= len(s2) - 1 and p3 >= len(s3) - 1
print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))