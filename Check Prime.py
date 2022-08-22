n=7
count=0
i=2
while(i<=n/2):
  if i%10==0:
    count+=1
  i+=1
if count==0:
   print("prime")
else:
   print("Not prime")