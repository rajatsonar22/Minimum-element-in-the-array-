'''# finding minimum element in array
#mninmum element
def get_min(arr,n):
    res = arr[0]
    for i in range (1,n):
        res = min (res,arr[i])
    return res
#maximum elementdef get max(arr,n):
def get_max(arr,n):
    res = arr[0]
    for i in range (1,n):
        res = max (res,arr[i])
    return res

#driver program
arr = [1,12,45,2,85,0]
n = len(arr)
print("MINIMUM ELEMENT:",get_min(arr,n))
print("MINIMUM ELEMENT:",get_max(arr,n))
'''
# maximum element
def get_min(arr,n):
    res = arr[0]
    for i in range (1,n):
        res = min(res,arr[i])
    return res

    # maximum element
def get_max(arr,n):
    res = arr[0]
    for i in range (1,n):
        res = max(res,arr[i])
    return res
arr = [1,55,222,5888,55]
n= len(arr)
print("MINIMUM ELEMENT:",get_min(arr,n))
print("MINIMUM ELEMENT:",get_max(arr,n))

