# from base import *
from base import icecoffee
from base import hotcoffee
from base import dessert



while True:
    print('─'*18)
    print('김지혜 홈카페 v0.1')
    print('─'*18)
    print('1. (ICE) 음료')
    print('2. (HOT) 음료')
    print('3. (ALL) 디저트')
    print('q. 종료')
    print('─'*18)
    no = input('메뉴를 선택하세요')

    if no == '1':
        icecoffee.icecoffeeMenu()
    elif no == '2':
        hotcoffee.hotcoffeeMenu()
    elif no == '3':
        dessert.dessertMenu()
    elif no == 'q':
        print('종료되었습니다')
        break
    else:
        print('선택 오류 다시 선택해 주세요')



