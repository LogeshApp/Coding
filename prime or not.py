#prime or not
a=input("Enter the number ")
if a!=2:
    for i in range (2,(a/2)+1):
        if(a%i==0):
            a=1
if a==1:
    print "Composite"
else:
    print "Prime"
