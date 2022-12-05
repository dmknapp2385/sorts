# array bubble_sort
 
# basic, not efficient

def bubbleSort(array):
    max_length = len(array) - 1

    for i in range(max_length):
        upper = max_length - i
        for j in range(0, upper):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [3,10, 50, 25, 15, 100, 150, 200, 250]

bubbleSort(array)


# more effiecient
