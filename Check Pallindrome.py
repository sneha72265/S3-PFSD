n=55
temp=n
rev=0
while n>0:
    r=int(n%10)
    rev=rev*10+r
    n=int(n/10)
if temp==rev:
    print("Palindrome")
else:
    print("not Pallindrome")