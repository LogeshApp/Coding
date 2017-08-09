#Code for Leap year or not
a=input("Enter the Year\n")
b=str (a)
if(a%400==0 or (a%4==0 and a%100!=0)):
    print( b + " is Leap Year")
else:
    print( b + " is not a Leap")


        
