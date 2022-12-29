"вариант 5"
"O(N log N)"
def merge_sort(a, flag = False):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        if flag:
            print(left)
            print(right)

        merge_sort(left,flag) 
        merge_sort(right,flag) 

        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                a[k] = left[i] 
                i+=1
            else: 
                a[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            a[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            a[k] = right[j] 
            j+=1
            k+=1