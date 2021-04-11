def merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right=arr[mid+1:high+1]
    i=0
    j=0
    # k is pointing to index
    # where we want to start merging
    k=low

    while i <len(left) and j< len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
            k=k+1
        else:
            arr[k]=right[j]
            j=j+1
            k=k+1
    while i < len(left):
        arr[k]=left[i]
        i=i+1
        k=k+1 
    while j < len(right):
        arr[k]=right[j]
        j=j+1
        k=k+1

