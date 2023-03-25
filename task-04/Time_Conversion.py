time=input()

time_list = time.split(':')

meridiem=""

time_len=2

meridiem=time[-time_len:]

print(meridiem)


time_list[0]

if meridiem=="PM":
    if int(time_list[0])<12:
        time_list[0]=str(int(time_list[0])+12)

if meridiem=="AM":
    if int(time_list[0])==12:
        time_list[0]="00"


print(time_list[0]+":"+time_list[1]+":"+time_list[2][:-2])
        
