# Health Management System
from datetime import datetime

def getdate():
    return datetime.now().time()

def createLog(clientName,fileName,log_content):
    with open('%s_%s.txt' % (clientName,fileName), 'a') as f:
        f.write(str(getdate())  + "  " + log_content +"\n")
    
dict1={1 : "Harry",2 : "Rohan", 3 : "Hammad"}
print("1 : Harry\n2 : Rohan\n3 : Hammad")
print("Choose a number for client:")
N=int(input())
print("1:Diet\n2:Exercise")
dict2={1:"Diet",2:"Exercise"}
print("Choose log file: ")
I=int(input())
try:
    print('Enter %s content for  %s' %(dict2[I],dict1[N]))
    content=input()
    createLog(dict1[N],dict2[I],content)
except Exception as e:
    print(str(e)+ " is invalid number")

    


    
     
 

