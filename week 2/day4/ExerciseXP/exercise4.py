import random


def compare_numbers(num):
    random_num = random.randint(1, 100)
    if num == random_num:
        return f"Congratulations! You guessed the right number: {num}"
    else:
        return f"Sorry, you didn't guess the right number. Your number: {num}, Random number: {random_num}"

number_input = int(input("Enter a number between 1 and 100: "))
print(compare_numbers(number_input))
