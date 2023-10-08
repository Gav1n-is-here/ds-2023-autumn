import random
from typing import List

def selectionSort(arr):
    countS=0
    n = len(arr)
    for i in range(n-1): 
        # 索引从0到n-2,每一轮在该位置都会放每轮找到的最小值
        minIndex = i
        for j in range(i+1,n):
            countS+=1
            if arr[j] < arr[minIndex]:  # 寻找最小数
                minIndex = j            # 将最小值的索引保存
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print('selectionsort runtime:',countS)
    return arr


def merge(arr1:List[int], arr2:List[int]):
    global countM 
    result = []
    while arr1 and arr2:
        countM+=1
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    return result

def merge_sort(arr:List[int]):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


lis = []
for j in range(5):
    lis.append([])
    for i in range(4*j+5):#4*j+5个元素
        lis[j].append(random.randint(0, 100))

for j in range(5):
    print("row",j,':')
    print('before',lis[j],'\n')
    countM=0
    print(selectionSort(lis[j]),'\n')
    merge_sort(lis[j])
    print('mergesort runtime:',countM)
    print(merge_sort(lis[j]))
    
    print('\n\n')




