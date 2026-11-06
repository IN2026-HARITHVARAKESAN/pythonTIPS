def calculate_mean(numbers):
    """Calculate the average of numbers."""
    if len(numbers) == 0:
       print("List cannot be empty")
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """Find the middle value after sorting."""
    if len(numbers) == 0:
       print("List cannot be empty")

    sorted_numbers = sorted(numbers)
    if len(sorted_numbers)%2==0:
        return (sorted_numbers[len(sorted_numbers)//2-1]+sorted_numbers[len(sorted_numbers)//2])/2
    else:
        return sorted_numbers[len(sorted_numbers)//2]
    
def calculate_mode(numbers):
    """Find the most frequently occurring value."""
    if len(numbers) == 0:
       print("List cannot be empty")
    sorted_numbers = sorted(numbers)
    current_number = sorted_numbers[0]
    current_count = 1
    max_count = 1
    modes = []
    for number in sorted_numbers[1:]:
        if number==current_number:
            current_count += 1
        else:
            if current_count>max_count:
                max_count = current_count
                modes = [current_number]
            elif current_count==max_count:
                modes.append(current_number)
            current_number = number
            current_count = 1
    return modes

def calculate_variance(numbers):
    """Calculate population variance."""
    if len(numbers) == 0:
       print("List cannot be empty")
    mean = calculate_mean(numbers)
    variance=0
    for number in numbers:
        variance += (number - mean) ** 2
    return variance / (len(numbers) - 1)


def calculate_standard_deviation(numbers):
    """Calculate population standard deviation."""
    variance = calculate_variance(numbers)

    return variance ** 0.5
