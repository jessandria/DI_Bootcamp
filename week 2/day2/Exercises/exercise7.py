favorite_fruits_input = input("Please enter your favorite fruit(s) separated by a single space: ")

favorite_fruits = favorite_fruits_input.split()

chosen_fruit = input("Now, please enter the name of any fruit: ")

if chosen_fruit in favorite_fruits:
   print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")
