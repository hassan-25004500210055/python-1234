# prime number
numbers=int(input("Enter the number: "))
cnt=0
for i in range(1,numbers+1):
        if numbers%i==0:
            cnt+=1
        if cnt>2:
            break
print(cnt)
if cnt==2:
       print("This is prime number :",numbers)
else:
       print("This is not prime number :",numbers)