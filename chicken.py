class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨]: {}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다")
        else:
            print("[대기번호 {}] {} 마리 주문이 완료됐습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError("준비한 재료가 모두 소진됐습니다.")
    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldOutError as err:
        print(err)
        break
