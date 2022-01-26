n=int(input("Enter the number"))
one=0
two=1
print("Fibonacci SERIES:")
print(one)
print(two)
for i in range(0,n+1):
    fib=one+two
    print(fib)
    one=two
    two=fib
