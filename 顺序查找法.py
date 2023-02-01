arr=[10,14,19,26,27,31,33,35,42,44]
def linear_search(value):
    for i in range(len(arr)):
        if arr[i]=value:
            return i
        return  -1

add= linear_search(26)
if add !=-1:
    print("查找成功，为序类中第%d个元素"%(add+1))
else:
    print("查找失败")
