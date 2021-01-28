from cx_Oracle import *
import sys

price = [4100,5400]
def hotcoffeeMenu():
    while True:
        print('─' * 18)
        print('(HOT) 음료 메뉴')
        print('─' * 18)
        print('1. 아메리카노', '4100원')
        print('2. 카페라떼  ', '5400원')
        print('q. 처음 화면')
        print('─' * 18)

        no = input('메뉴를 선택하세요')

        if no == '1':
            hotAmenum = int(input('원하는 개수 선택'))
            ha = hotAmenum * price[0]
            print('총', hotAmenum, '잔', ha, '원')
            print('주문완료')
            print('─' * 22)
            import time
            print('─' * 22)
            print('HOT 아메리카노 제조 시작')
            for x in range(2):
                time.sleep(1)
            print('HOT 아메리카노 제조 완료! ')
            print('─' * 22)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            print('─' * 22)
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
            hotRanum = int(input('원하는 개수 선택'))
            hr = hotRanum * price[1]
            print('총', hotRanum, '잔', hr, '원')
            print('주문완료')
            print('─' * 22)
            import time
            print('─' * 22)
            print('HOT 카페라떼 제조 시작')
            for x in range(2):
                time.sleep(1)
            print('HOT 카페라떼 제조 완료! ')
            print('─' * 22)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            print('─' * 22)
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
