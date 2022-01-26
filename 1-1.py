start=int(input("Enter the start year"))
end=int(input("Enter the end year"))
print("leap years")
for i in range(start,end):
    if i%4 ==0 or i%100==0 or i %400==0 :
        print(i)

