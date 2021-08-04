#Pattern Matching

print("Enter number of rows")
n=int(input())
print("Enter Boolean value ")
b=bool(int(input()))
print(b)
i=0
if b==True:
    while(i<=n):
        print("* "*i)
        i+=1 
if b==False:
    while(n>i):
        print("* "*n)
        n-=1

    
     
 

