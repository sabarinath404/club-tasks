number=int(input())

number_row=input()
candle_count=0

A=[]

list_obj = number_row.split()
row = list(map(int, list_obj))

for i in range(number):
    A.append(row[i])



max = A[0]; 
     
   
for i in range(0, len(A)):    
   if(A[i] > max):    
       max = A[i];    

for i in range(0, len(A)):     
    if(A[i] == max):
        candle_count+=1

print(candle_count)
        
