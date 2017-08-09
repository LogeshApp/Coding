#palindrome
a=input("Enter the number")
b=a
c=0
while a>0:
    c=c*10+a%10
    a=a/10
if b==c:
    print "Palindrome"
else:
    print "Not palindrome:"
