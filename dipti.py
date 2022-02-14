s="the is largest number"
spilt_value= []
b=''
count=0
for i in s:
    if i==' ':
        print(count)
        count=0
        spilt_value.append(b)
        b =''
    else:
        b=b+i
        count=count+1
if b:
    spilt_value.append(b)
    print(spilt_value)

