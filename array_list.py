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
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                swap_values(array, i, j)
    return array

def linear_search(array_list,target):
    for i in range(len(array_list)):
        if array_list[i] == target:
            return True
    return False

def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

if __name__ == "__main__":
    array_list = generate_values(10)