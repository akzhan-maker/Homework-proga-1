def max_subarray_sum(nums, k):
    max_sum = -1
    found = False
    for i in range(len(nums) - k + 1):
        window = nums[i: i + k]
        is_valid = True
        current_sum = 0
        for x in window:
            if x <= 0:
                is_valid = False
                break
            current_sum += x
        if is_valid:
            if current_sum > max_sum:
                max_sum = current_sum
            found = True
    return max_sum if found else None
numbers = [1, 2, 3, -1, 4, 5, 0, 6, 7]
k = 2
result = max_subarray_sum(numbers, k)
print( result)  # Вывод: 13