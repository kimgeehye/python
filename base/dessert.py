from cx_Oracle import *
import sys

price = [5000,5500]
def dessertMenu():
    while True:
        print('─' * 18)
        print('(ALL) 디저트')
        print('─' * 24)
        print('1. 에  그 샌드위치', '5000원')
        print('2. 베이컨 샌드위치', '5500원')
        print('q. 처음 화면')
        print('─' * 24)

        no = input('메뉴를 선택하세요')

        if no == '1':
            eggSannum = int(input('원하는 개수 선택'))
            es = eggSannum * price[0]
            print('총', eggSannum, '개', es, '원')
            print('주문완료\n샌드위치 준비 완료!')
            print('─'* 24)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            print('─' * 24)
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
            baconSannum = int(input('원하는 개수 선택'))
            bs = baconSannum * price[1]
            print('총', baconSannum, '개', bs, '원')
            print('주문완료\n샌드위치 준비 완료!')
            print('─' * 24)
            jm = input('1. 주문 계속 진행\n2. 주문 종료\n선택')
            print('─' * 24)
            if jm == '1':
                print('1. 주문 계속 진행')
                break
            elif jm == '2':
                print('주문 종료')
                sys.exit()
            else:
                print('잘못 입력하셨습니다 시스템 자동 종료됩니다')
                sys.exit()

        else:
            print('잘못 입력하셨습니다 다시 입력해 주세요')


