def prime(num):
    i=1
    count=0
    while(i<=num):
        if num%i==0:
            count+=1
        i+=1
    if(count==2):
        print(num)
j=1
while(j<=100):
    prime(j)
    j+=1