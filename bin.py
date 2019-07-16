                                            BINARY TO DECIMAL IN REVERSE 
arr=[]
n=int(input("Enter the number:"))
rev= 0    
while(n > 0):    
    Rem = n %10    
    rev = (rev *10) + Rem   
    n = n //10    
while rev!=0:
    temp=rev%2
    arr.append(temp)
    rev=rev//2
arr.reverse()
for i in arr:
  print(i,end=" ")
ENTER THE NUMBER:25
110100
