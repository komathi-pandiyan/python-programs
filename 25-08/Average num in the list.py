def calculate_average(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0 
    average = total_sum / count
    return average


numbers_list = [12, 45, 23, 6, 78, 34, 89]

average = calculate_average(numbers_list)
print("Average:", average)
