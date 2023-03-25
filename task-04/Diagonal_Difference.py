



def diagonal_difference():
    n = int(input())
    arr = []
    for i in range(n):
        row = list(map(int, input().rstrip().split()))
        arr.append(row)
    
    d1_sum = 0
    d2_sum = 0
    for i in range(n):
        d1_sum += arr[i][i]
        d2_sum += arr[i][n-i-1]
    
    return abs(d1_sum - d2_sum)
print(diagonal_difference())
    

