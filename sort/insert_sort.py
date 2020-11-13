def insertSort(arr):
    for x in range(1,len(arr)):
        # 当前位置
        for j in range(x-1,-1,-1):
            if arr[j]<=arr[j+1]:
                break
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] =temp
        # num = arr[x]
        # while j >=0 and num < arr[j] :
        #     arr[j+1] = arr[j]
        #     j-=1
        # arr[j+1] = num
    return arr

arr = [2,1,8,7,4,6]
insertSort(arr)
print(arr)


