list=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=0
a=[]
while i<len(list):
    for j in list[i]:
        a.append(list[i][j])
        i=i+1
print(a)
        
