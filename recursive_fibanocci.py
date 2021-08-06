def recursive_fibanocci(n):
    if n==0:
        return 1
    elif n==1:
        return 1 
    else :
        return recursive_fibanocci(n-1)+recursive_fibanocci(n-2)

n=int(input("Enter a number:"))
print(recursive_fibanocci(n))
