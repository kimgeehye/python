from base.common import *
from cx_Oracle import *
import sys

price = [4100,5400,6000,6000]
def icecoffeeMenu():
    while True:
        print('─' * 18)
        print('(ICE) 음료 메뉴')
        print('─' * 18)
        print('1. 아메리카노', '4100원')
        print('2. 카페라떼  ', '5400원')
        print('3. 밀크쉐이크', '6000원')
        print('4. 망고스무디', '6000원')
        print('q. 처음 화면')
        print('─' * 18)

        no = input('메뉴를 선택하세요')

        if no == '1':
            iceAmenum = int(input('원하는 개수 선택'))
            iaa = iceAmenum * price[0]
            print('총', iceAmenum, '잔', iaa, '원')
            print('주문완료')
            print('─' * 20)
            import time
            print('─' * 20)
            print('아메리카노 제조 시작')
            for x in range(2):
                time.sleep(1)
            print('아메리카노 제조 완료!')
            print('─' * 20)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            print('─' * 20)
            if jm == '1':
                print('1. 주문 계속 진행')
                break
            elif jm == '2':
                print('주문 종료')
                sys.exit()
            else:
                print('잘못 입력하셨습니다 시스템 자동 종료됩니다')
                sys.exit()

        elif no == '2':
            iceRanum = int(input('원하는 개수 선택'))
            ir = iceRanum * price[1]
            print('총', iceRanum, '잔', ir, '원')
            print('주문완료')
            print('─' * 20)
            import time
            print('─' * 20)
            print('카페라떼 제조 시작')
            for x in range(2):
                time.sleep(1)
            print('카페라떼 제조 완료!')
            print('─' * 20)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            print('─' * 20)
            if jm == '1':
                print('1. 주문 계속 진행')
                break
            elif jm == '2':
                print('주문 종료')
                sys.exit()
            else:
                print('잘못 입력하셨습니다 시스템 자동 종료됩니다')
                sys.exit()

        elif no == '3':
            iceMilknum = int(input('원하는 개수 선택'))
            im = iceMilknum * price[2]
            print('총', iceMilknum, '잔', im, '원')
            print('주문완료')
            print('─' * 20)
            import time
            print('─' * 20)
            print('밀크쉐이크 제조 시작')
            for x in range(2):
                time.sleep(1)
            print('밀크쉐이크 제조 완료!')
            print('─' * 20)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            if jm == '1':
                print('1. 주문 계속 진행')
                break
            elif jm == '2':
                print('주문 종료')
                sys.exit()
            else:
                print('잘못 입력하셨습니다 시스템 자동 종료됩니다')
                sys.exit()

        elif no == '4':
            iceMangnum = int(input('원하는 개수 선택'))
            ims = iceMangnum * price[3]
            print('총', iceMangnum, '잔', ims, '원')
            print('주문완료')
            print('─' * 20)
            import time
            print('─' * 20)
            print('망고스무디 제조 중')
            for x in range(2):
                time.sleep(1)
            print('망고스무디 제조 완료!')
            print('─' * 20)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            if jm == '1':
                print('1. 주문 계속 진행')
                break
            elif jm == '2':
                print('주문 종료')
                sys.exit()
            else:
                print('잘못 입력하셨습니다 시스템 자동 종료됩니다')
                sys.exit()

        elif no == 'q':
            break
        else:
            print('잘못 선택하셨습니다.')