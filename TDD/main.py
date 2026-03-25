def add_numbers(numbers):
    return sum(map(int, numbers.replace('\n',',').split(','))) if numbers else 0