# selections sort 

def selectionSort(array):
    mxLength = len(array)
    for i in range(mxLength):
        min_index = i
        for j in range(i+1, mxLength):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]

    print(array)

array = [2, 5, 1, 4, -1, 0,  10, 25, 30, 150, 100]
selectionSort(array)