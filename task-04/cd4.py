number =int(input())
list_obj = []
count=0
for i in range(number):
    line=input()
    list_obj.append(line)


for i in range(number):
    if '+' not in list_obj[i]:
        count=count-1
    else:
        count=count+1

print(count)