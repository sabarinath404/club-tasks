
A =[]
B =[]

pointA=0
pointB=0

a= input()

split_a=a.strip().split(' ')



b= input()
split_b=b.split(" ")

my_listA = a.split()
list_objectA = list(map(int, my_listA))

my_listB = b.split()
list_objectB = list(map(int, my_listB))

for i in range(3):

    A.append(list_objectA[i])
    B.append(list_objectB[i])



print(A)
print(B)






for i in range(3):
    if A[i] > B[i]:
        pointA+=1
    elif A[i] < B[i]:
        pointB+=1


print(pointA,pointB)