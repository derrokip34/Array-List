import random

def generate_values(size):
    array_list = []
    for i in range(size):
        array_list.append(random.randrange(1, 100))
    return array_list