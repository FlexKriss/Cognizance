print("This program checks if a given number is a Palindrome or not")
reverse = 0
print("Enter number")
num = int(input("> "))
temp = num
while (temp > 0):
    a = temp%10
    reverse = reverse*10 + a
    temp = temp//10
if(num == reverse):
    print("Given number is a Palindrome")
else:
    print("Given number is not a Palindrome")