print("Fibonacci Series using iteration\n")
n=int(input("Enter the number of terms you want in the Fibonacci series : "))
a=0
b=1
print("Fibonacci series is : ",end="")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    