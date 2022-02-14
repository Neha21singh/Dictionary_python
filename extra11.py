i=2
a=[]
while i<=30:
    j=2
    count=0
    while j<i:
        if i%j==0:
            count=count+1
        j=j+1

    if count==0:
        a.append(i)
    if a[i]%10==0:
        a=a//10
    i=i+1
k=a[0:4]
c=a[4:12]
print(a)
