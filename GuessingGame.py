import random
print("Hello Mr.X welcome to Guessing Game")
a=random.randint(0,100)
Guess_count=0
 
while(Guess_count < 10):
    print("Enter your guess")
    inp1=int(input())
    if(inp1==a):
        print("Congrats, you won the game")
        break
    elif(inp1>a):
        print("the number you are searching is smaller than ",inp1)
    elif(inp1<a):
        print("the number you are searching is greater than",inp1)
        
    Guess_count=Guess_count+1
    
if(Guess_count==10):
    print("Sorry,Try later")
else:
    print("Mr.X guessed the number in ",Guess_count,"Counts")
     
 

