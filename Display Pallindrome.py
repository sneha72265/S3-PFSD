num=1
while num<=100:
    temp=num
    rev=0
    while(temp>0):
        r=int(temp%10)
        rev=(rev*10)+r
        temp=int(temp/10)
    if(num==rev):
        print(num)
    num=num+1