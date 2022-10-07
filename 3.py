import random

stone = random.randint(3,30)
print(stone)
while stone > 0:
    b = int(input())
    if 1 <= b and b <= 3 and b < stone:
        stone = stone - b
        print('ваш ход',b, 'остаток', stone)
        if stone <= 1:
            print('вы выиграли')
        else:
            c = random.randint(1, 3)
            if c > stone:
                print('вы выиграли')
            else:
                stone -= c
                print('ход компьютера',c, 'остаток', stone)
                if stone == 1:
                    print('Вы проиграли')
    else:
        print('неверное число')
