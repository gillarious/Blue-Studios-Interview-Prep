# Search and Sorting Algorithms

## Binary Search

### Implementation

```python
def binary_search(alist, start, end, item):
    dist = end - start
    midpoint = dist // 2 + start
    if midpoint == len(alist):
        midpoint -= 1
    if alist[midpoint] == item:
            return True
    elif dist <= 0:
        return False
    else:
        if item < alist[midpoint]:
            return binary_search(alist, start, midpoint, item)
        else:
            return binary_search(alist, midpoint+2, end, item)
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| algorithm        | O(logN)         |

---

## Bubble Sort

### Implementation

```python
def bubbleSort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(0, n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| algorithm        | O(N^2)         |

---

## QuickSort

### Implementation

```python
def partition(arr, low, high): 
    i = (low-1)         
    pivot = arr[high]  
    for j in range(low, high): 
        if arr[j] <= pivot: 
            i = i+1 
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 

def quickSort(arr, low, high): 
    if low < high: 
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| algorithm        | O(NlogN)         |

---

## Merge Sort

### Implementation

```python
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0, n1): 
        L[i] = arr[l + i] 
    for j in range(0, n2): 
        R[j] = arr[m + 1 + j] 
    i = 0    
    j = 0    
    k = l   
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

def mergeSort(arr, l, r): 
    if l < r: 
        m = (l + (r-1)) / 2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| algorithm        | O(NlogN)         |