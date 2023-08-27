def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  
        
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    
    return -1  
sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18]
target_element = 10
index = binary_search(sorted_array, target_element)
if index != -1:
    print(f"Element {target_element} found at index {index}.")
else:
    print(f"Element {target_element} not found in the array.")
