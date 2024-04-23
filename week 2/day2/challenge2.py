word = str(input("Enter a word: "))
n = word[0]

for char in word[1:]:
    if char != n[-1]:
        n = n+char 

print(n)

