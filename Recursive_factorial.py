#Recursive function that implements factorial function
def recursive_factorial(n):
    if n==1:
        return 1 
    else :
        return recursive_factorial(n-1)*n

n=int(input("Enter a number:"))
print(recursive_factorial(n))
