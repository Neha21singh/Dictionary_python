dict1=[2,4,5,7]
i=0
sum=0
c={}
while i<len(dict1):
    sum=sum+dict1[i]
    c[i]=sum
    i=i+1
print(c)
