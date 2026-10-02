numbers = [10, 20, 30, 40, 50]
target = 40

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found at index:", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1