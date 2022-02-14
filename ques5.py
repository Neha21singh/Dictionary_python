x=["one","two","three","four","five"]
y=[1,2,3,4,5,]
i=0
c={}
while i<len(x):
    c.update({x[i]:y[i]})
    i=i+1
print(c)