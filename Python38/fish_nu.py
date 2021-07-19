# fish_nu
#  20.08.13 - начальные услоаия

# 0 - отсутствие
# 1 - белый
# 2 - черный

# 1 - пешка
# 2 - ладья
# 3 - конь
# 4 - слон
# 5 - ферзь
# 6 - король
# 7 - 0 - 0
# 8 - 0 - 0 - 0
# 9 - пешка - перевертыш

import fish_utils as ut
import fish_utils_check as utc
import fish_utils_turn as utt
import numpy as np

d = fish_D
x = 8
y = 8
c = 2
desk = np.zeros((x, y, c),'int8')

desk[6,0,0] = 6 # король
desk[6,0,1] = 1 # белый
desk[2,4,0] = 5 # ферзь
desk[2,4,1] = 1 # белый
desk[6,7,0] = 6 # король
desk[6,7,1] = 2 # черный
desk[0,7,0] = 2 # ладья
desk[0,7,1] = 1 # белый
desk[4,7,0] = 4 # слон
desk[4,7,1] = 1 # белый

n = 1 # ход
v = 0 # варианты
sw = 'Белые  : '
sb = 'Черные : '

sw, sb = ut.fish_position_list(x, y, desk)
print(sw)
print(sb)

ikb, jkb = utc.king_black(x, y, desk)
print('король черный ', ikb, jkb)
ikw, jkw = utc.king_white(x, y, desk)
print('король белый ', ikw, jkw)
c = 2
f, i, j = utc.king_check(c, x, y, ikw, jkw, desk)
print('угроза белому королю. ', f, i, j)
c = 1
f, i, j = utc.king_check(c, x, y, ikb, jkb, desk)
print('угроза черному королю. ', f, i, j)

#v = utt.turn(v, n, x, y, desk)