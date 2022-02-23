print("This program will print characters that have an even index")
print("Enter a string")
a = str(input("> "))
index = 0
while index < len(a):
    print(a[index], end="")
    index += 2