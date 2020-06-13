from random import *

idlist = []

for i in range(1, 21):
    idlist.append(i)

idlist = set(idlist)
chicken = sample(idlist, 1)
chicken = set(chicken)
idlist = idlist.difference(chicken)
coffee = sample(idlist, 3)
print("-- 당첨자 발표 --")
print("치킨 당첨자: ", list(chicken)[0])
print("커피 당첨자: ", coffee)
print("-- 축하합니다 --")
