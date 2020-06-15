from random import *

dict = {}
i = 1
while (i < 51):
    dict[i] = randrange(5, 51)
    i += 1

sum = 0
i = 1
while (i < 51):
    check = '0' if 5<= dict[i] <= 15 else ' '
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i, dict[i]))
    if check == '0':
        sum += 1
    i += 1
print("총 탑승 승객: {}분".format(sum))

#passenger = list(range(1, 51))
#passenger = [randrange(5, 51) for i in passenger]
#i = 0
#sum = 0
#while (i < 50):
#    check = 'O' if 5 <= passenger[i] <= 15 else ' '
#    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i+1, passenger[i]))
#    i += 1
#    if check == 'O':
#        sum += 1
#print("총 탑승 승객: {}분".format(sum))
