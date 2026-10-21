numbers=int(input("Enter the number: "))
rev=0
rem=None
temp=numbers
while(numbers!=0):
    rem=numbers%10
    rev=(rev*10) + rem
    numbers=numbers//10
if temp==rev:
    print("This is palindrome number")
else:
    print("This is not palindrome number")