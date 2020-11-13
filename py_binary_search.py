
count = 0
def binarySerach(arr,num, l,r):
    global count 
    count+=1
    mid = int((l+r)/2)
    if l == mid:
        return -1
    if arr[mid] == num:
        return mid
    if arr[mid] > num :
       return binarySerach(arr,num,l,mid)
    else :
        return binarySerach(arr,num,mid,r)

arr = range(0,1024)
print(binarySerach(arr,78,0,len(arr) - 1))
print(count)


    

