from random import *

passenger = list(range(1, 51))
passenger = [randrange(5, 51) for i in passenger]
i = 0
sum = 0
while (i < 50):
    check = 'O' if 5 <= passenger[i] <= 15 else ' '
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i+1, passenger[i]))
    i += 1
    if check == 'O':
        sum += 1
print("총 탑승 승객: {}분".format(sum))
    
