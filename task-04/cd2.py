number_inp=int(input())

my_list = []

for _ in range(number_inp):
    my_list.append(input())


for i in range (len(my_list)):
     if (len(my_list[i])>10):
          
           print(((my_list[i])[0])+str((len(my_list[i]))-2)+(my_list[i])[-1])
     else:
          print(my_list[i])

   