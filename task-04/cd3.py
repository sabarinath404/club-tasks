Count_number = input()
first_input=[]
number=[]
count=0


cont_list = Count_number.split()

for i in range (len(cont_list)):
        first_input.append(cont_list[i])


        
       
num_sequence = input()

num_list = num_sequence.split()

# for i in range (len(num_list)):
#         number.append(num_list[i])

cont_list = list(map(int, cont_list))
num_list = list(map(int, num_list))

# for i in range (len(num_list)):
#     if cont_list[1] ==1:

#         if num_list[i] >= cont_list[1]:
#             count+=1
          
#     elif num_list[i] > cont_list[1]:

#      count+=1



# print(count)
    



# n,k = map(int,input().split())

temp = num_list[(cont_list[1])-1]
count=0
for i in range(0,len(num_list)):
    if num_list[i]>=temp and num_list[i]>0 :
        count+=1
print(count)