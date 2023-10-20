def productExceptSelf(nums):
    #Create products calculated from both directions
    forwardProducts = []
    curProd = 1
    for num in nums:
        curProd *= num
        forwardProducts.append(curProd)
    
    backwardProducts = []
    curProd = 1
    for num in reversed(nums):
        curProd *= num
        backwardProducts.append(curProd)
    #because we read through the array backwards but we append to the end of the list, we should flip it
    backwardProducts.reverse()

    #Pad the prefix/suffix arrays
    forwardProducts = [1] + forwardProducts + [1]
    backwardProducts = [1] + backwardProducts + [1]
    
    #Calculate the product for all indicies execpt the current one
    ans = []
    for i in range(len(nums)):
        #because of padding product indicies are +1
        product = forwardProducts[i] * backwardProducts[i+2]
        ans.append(product)
    
    return ans

print(productExceptSelf([1,2,3,4]))