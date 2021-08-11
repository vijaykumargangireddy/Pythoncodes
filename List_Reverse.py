a=["apple","banana","pine-apple"]
i=0
while(i<len(a)/2):
    a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
    i+=1
print(a)
    
