#rock_paper_scissor
import random
entities=["r","p","s"]
print("welcome to the rock_paper_scissor game")
Trails=1
User_Points=0 
Comp_Points=0 
 
 
while(Trails<10):
    game_input=input("Enter your choice \n r:Rock \n p:Paper \n s:Scissor\n")
    computer_input=random.choice(entities)
    
    if((game_input=="r" and computer_input =="s") or (game_input=="s" and computer_input=="p") or (game_input=="p" and computer_input=="r")):
        User_Points+=1 
        print("User input is %s Computer input is %s"%(game_input,computer_input))
        print("User gained point")
    elif((game_input=='p'and computer_input =='s') or (game_input=='r' and computer_input=='p') or (game_input=='s' and computer_input=='r')):
        Comp_Points+=1 
        print("User input is %s Computer input is %s"%(game_input,computer_input))
        print("Computer gained point")
    elif(game_input==computer_input):
        print("user input is same as computer input")
    
        
    else:
        print("Please check your Inputs:")
        continue
    Trails+=1
    
if(Comp_Points>User_Points):
    print("Computer Won with %s" %Comp_Points)
elif(Comp_Points==User_Points):
    print("Tie")
else:
    print("User Won With %s" %User_Points)


