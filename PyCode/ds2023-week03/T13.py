import random
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
 
if __name__ == '__main__':
    array =[]
    for i in range(15):
        array.append(random.randint(0, 100))
    print('origin:',array)
    print(selectionSort(array))
#时间复杂度：
#那么交换的次数为0次
#则时间为(n-1)*t,即最优时间复杂度为O(n)。
#最差情况：当前数列全为逆序
#那么交换的次数为n-1次
#则时间为n*(n-1)*t，即O(n²)。
#取平均时间复杂度，则选择排序时间复杂度为O(n²)。

#空间复杂度：
#最好的情况：不需要交换，
#那么空间复杂度为0
#最坏的情况：全为逆序数
#那么整个过程就需要temp，i，j，k临时变量，即为4
#取平均值可以得到选择排序的空间复杂度为O(1)。