print("This program makes and does (i) in a 2-d list")
print("Enter number of rows required, [including Title row]")
row = int(input("> "))
i = 1
List = [[]]
a = "R"
b = "Name"
c = "Mark"
while i <= row:
    n_list = [[a, b, c]]
    print("Enter roll number")
    a = int(input("> "))
    print("Enter name")
    b = input("> ")
    print("Enter marks")
    c = int(input("> "))
    List = List + n_list
    i += 1

for row in List:
    print(*row, sep=" ")

# i tried to make the table look more neat by spacing etc
# and struggled for about 30 minutes and couldn't figure it out

