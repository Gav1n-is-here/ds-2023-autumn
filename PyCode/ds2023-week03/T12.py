import random
def insertion_sort(array):
    for i in range(len(array)):
        cur_index = i
        while array[cur_index-1] > array[cur_index] and cur_index-1 >= 0:
            array[cur_index], array[cur_index-1] = array[cur_index-1], array[cur_index]
            cur_index -= 1
            print(array)
    return array
 
 
if __name__ == '__main__':
    array =[]
    for i in range(15):
        array.append(random.randint(0, 100))
    print('origin:',array)
    insertion_sort(array)