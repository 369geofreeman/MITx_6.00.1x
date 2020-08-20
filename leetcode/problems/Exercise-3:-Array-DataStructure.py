# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function



x = input('Enter a nunmber: ')

[print(i) for i in range(int(x)) if i%2!=0]
