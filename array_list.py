import random
import time

class ArrayList:
    def __init__(self, size):
        self.array_list = [random.randrange(1, 100) for _ in range(size)]

    def swap_values(self, a, b):
        temp = self.array_list[a]
        self.array_list[a] = self.array_list[b]
        self.array_list[b] = temp

    def sort_array(self):
        for i in range(len(self.array_list)):
            for j in range(len(self.array_list)):
                if self.array_list[i] < self.array_list[j]:
                    self.swap_values(i, j)

    def linear_search(self, target):
        for i in range(len(self.array_list)):
            if self.array_list[i] == target:
                return True
        return False

    def binary_search(self, target):
        low, high = 0, len(self.array_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array_list[mid] == target:
                return True
            elif self.array_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def repeat_search_function(self, search_method, target_value, iterations):
        total_time = 0
        for _ in range(iterations):
            start = time.time()
            search_result = search_method(target_value)
            end = time.time()
            total_time += (end - start)

        if search_result:
            print(f"{target_value} found")
        else:
            print(f"{target_value} not found")

        avg_time = total_time / iterations

        return avg_time

if __name__ == "__main__":
    list_sizes = [100, 300, 800]
    for size in list_sizes:
        array_list_obj = ArrayList(size)

        target_value = random.choice(array_list_obj.array_list)

        linear_search_time = array_list_obj.repeat_search_function(array_list_obj.linear_search, target_value, 1000)
        print(f"Linear Search Time for size {size}: {linear_search_time:.10f} seconds")

        array_list_obj.sort_array()
        binary_search_time = array_list_obj.repeat_search_function(array_list_obj.binary_search, target_value, 1000)
        print(f"Binary Search Time for size {size}: {binary_search_time:.10f} seconds")
