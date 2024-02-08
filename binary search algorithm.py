from colorama import Fore
import time
from tqdm import tqdm
import random

# panjeet 
def get_input(message):
    return input(message)

def get_numeric_input():
    while True:
        num = input("Enter a number to add to the array (! to stop): ")
        if num == '!':
            return None
        try:
            return int(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_string_input():
    while True:
        string = input("Enter a string to add to the array (! to stop): ")
        if string == '!':
            return None
        if any(char.isdigit() for char in string):
            print("Invalid input. Please enter a valid string without numbers.")
        else:
            return string

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    indices = []

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            indices.append(mid)
            # Continue searching for more occurrences
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return indices

def main():
    array_type = get_input("Enter 'num' for numeric sequence or 'str' for string sequence: ")

    input_functions = {'num': get_numeric_input, 'str': get_string_input}

    if array_type not in input_functions:
        print("Invalid input. Please enter 'num' or 'str'.")
        return

    input_function = input_functions[array_type]

    array = []

    while True:
        element = input_function()
        if element is None:
            break
        array.append(element)

    array.sort()

    target_element = input("Enter the element you are looking for (! to exit): ")

    try:
        if array_type == 'num':
            target_element = int(target_element)
        else:
            if any(char.isdigit() for char in target_element):
                raise ValueError("Invalid input. Please enter a valid string without numbers.")
        indices = binary_search(array, target_element)
    except ValueError as e:
        print(e)
        return

    if indices:
        indices = [index + 1 for index in indices]
        print(f"{target_element} found at indice(s): {', '.join(map(str, indices))}.")
    else:
        print(f"{target_element} not found in the array.")

if __name__ == "__main__":
    print(Fore.WHITE + "Welcome, loading....\n")
    for i in tqdm(range(100)):
        time.sleep((random.randint(0, 6) / 100))
    main()
