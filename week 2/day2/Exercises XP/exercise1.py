my_fav_numbers = {7, 11, 23, 42}

my_fav_numbers.add(3)
my_fav_numbers.add(17)

my_fav_numbers.remove(17)

friend_fav_numbers = {5, 13, 19, 31}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

