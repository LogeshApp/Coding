#Display even numbers between Given two intervals
a=input("Enter starting of interval")
b=input("Enter ending of interval")
for i in range(a,b):
    if i%2==0:
        print i
