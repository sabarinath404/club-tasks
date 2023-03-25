line=input()
count=0

status = False
for i in range (len(line)):
    s_string = line[i:i+7]
    if s_string == '1111111' or s_string == '0000000':
       status=True
       
if status:
    print("YES")
else:
    print("NO")
    
        
        