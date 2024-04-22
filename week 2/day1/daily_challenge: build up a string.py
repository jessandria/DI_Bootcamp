user_string = input("Enter a string of exactly 10 characters: ")

if len(user_string) < 10:
    print("String not long enough")

elif len(user_string) > 10:
    print("String too long")
else:
    print("Perfect string")
    print("First character:",user_string[0])
    print("Last character:",user_string[-1])


for x in user_string:
    print(x, end="")



    
    
    