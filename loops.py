# while loop 

count = 0

while count < 3:
    count = count + 1
    print("Hello Geek")

# Single Statement While Loop

count = 0

while count == 0:
    print("Hello Geek")

# For Loop — List Iteration

print("List Iteration")

l = ["geeks", "for", "geeks"]

for i in l:
    print(i)

# For Loop — Tuple Iteration

print("Tuple Iteration")

t = ("geeks", "for", "geeks")

for i in t:
    print(i)

# For Loop — String Iteration

print("String Iteration")

s = "Geeks"

for i in s:
    print(i)

# Iterating by Index

list = ["geeks", "for", "geeks"]

for index in range(len(list)):
    print(list[index])


# Continue Statement

for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue

    print("Current Letter:", letter)

# Break Statement

for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        break

    print("Current Letter:", letter)
