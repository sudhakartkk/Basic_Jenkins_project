import math

def average(list_of_numbers):
    if not list_of_numbers:
        return 0
    return sum(list_of_numbers) / len(list_of_numbers)