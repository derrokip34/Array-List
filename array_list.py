import random

def generate_values(size):
    array_list = []
    for i in range(size):
        array_list.append(random.randrange(1, 100))
    return array_list

def swap_values(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def sort_array(array):
    for i in range(len(array)-1):  # Correcting the loop condition
        if array[i] > array[i+1]:
            swap_values(array, i, i+1)
    return array