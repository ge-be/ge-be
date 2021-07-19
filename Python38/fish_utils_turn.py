# fish_utils_turn
#  20.08.14 - файл функкций  ходов jпроекта fish
# *************************************************************************

import fish_utils as ut

# *************************************************************************
def turn_pawn(v, n, i, j, f):
# пешка белая
    i_t = i
    j_t = j + 1
    if j_t < 7:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        if j == 1:
            j_t = j + 2
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
# взятие на проходе добавить
        elif j == 4:
            i_t = i + 1
            if i_t < 7:
                v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
            i_t = i - 1
            if i_t >= 0:
                v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
# превращение добавить
        elif j == 6:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, 9)
    return v

# *************************************************************************
def turn_rook(v, n, i, j, f):
# ладья
    j_t = j
    i_t = i - 1  # влево 1
    if i_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 2  # влево 2
    if i_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 3  # влево 3
    if i_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 4  # влево 4
    if i_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 5  # влево 5
    if i_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 6  # влево 6
    if i_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 7  # влево 7
    if i_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    # ввверх-вниз
    i_t = i
    j_t = j - 1  # вниз 1
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 1  # вверх 1
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 2  # вниз 2
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 2  # вверх 2
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 3  # вниз 3
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 3  # вверх 3
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 4  # вниз 4
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 4  # вверх 4
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 5  # вниз 5
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 5  # вверх 5
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 6  # вниз 6
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 6  # вверх 6
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 7  # вниз 7
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 7  # вверх 7
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
# вправо
    j_t = j
    i_t = i + 1  # вправо 1
    if i_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 2  # вправо 2
    if i_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 3  # вправо 3
    if i_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 4  # вправо 4
    if i_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 5  # вправо 5
    if i_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 6  # вправо 6
    if i_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 7  # вправо 7
    if i_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    return v

# *************************************************************************
def turn_knight(v, n, i, j, f):
    i_t = i - 1  # влево 1
    if i_t >= 0:
        j_t = j - 2
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 2
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 2  # влево 2
    if j_t >= 0:
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 1  # вправо 1
    if i_t < 8:
        j_t = j - 2
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 2
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 2  # вправо 2
    if i_t < 8:
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    return v

# *************************************************************************
def turn_beshop(v, n, i, j, f):
# слон
    i_t = i - 1  # влево 1
    if i_t >= 0:
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 2  # влево 2
    if i_t >= 0:
        j_t = j - 2
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 2
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 3  # влево 3
    if i_t >= 0:
        j_t = j - 3
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 3
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 4  # влево 4
    if i_t >= 0:
        j_t = j - 4
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 4
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 5  # влево 5
    if i_t >= 0:
        j_t = j - 5
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 5
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 6  # влево 6
    if i_t >= 0:
        j_t = j - 6
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 6
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 7  # влево 7
    if i_t >= 0:
        j_t = j - 7
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 7
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
# вправо
    i_t = i + 1  # вправо 1
    if i_t < 8:
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 2  # вправо 2
    if i_t < 8:
        j_t = j - 2
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 2
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 3  # вправо 3
    if i_t < 8:
        j_t = j - 3
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 3
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 4  # вправо 4
    if i_t < 8:
        j_t = j - 4
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 4
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 5  # вправо 5
    if i_t < 8:
        j_t = j - 5
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 5
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 6  # вправо 6
    if i_t < 8:
        j_t = j - 6
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 6
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 7  # вправо 7
    if i_t < 8:
        j_t = j - 7
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 7
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    return v

# *************************************************************************
def turn_queen(v, n, i, j, f):
# ферзь
    i_t = i - 1 # влево 1
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 2 # влево 2
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 2
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 2
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 3 # влево 3
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 3
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 3
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 4 # влево 4
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 4
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 4
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 5 # влево 5
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 5
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 5
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 6 # влево 6
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 6
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 6
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i - 7 # влево 7
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 7
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 7
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
# ввверх-вниз
    i_t = i
    j_t = j - 1 # вниз 1
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 1 # вверх 1
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 2 # вниз 2
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 2 # вверх 2
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 3 # вниз 3
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 3 # вверх 3
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 4 # вниз 4
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 4 # вверх 4
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 5 # вниз 5
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 5 # вверх 5
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 6  # вниз 6
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 6 # вверх 6
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j - 7 # вниз 7
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 7 # вверх 7
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
# вправо
    i_t = i + 1 # вправо 1
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 2 # вправо 2
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 2
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 2
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 3 # вправо 3
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 3
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 3
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 4 # вправо 4
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 4
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 4
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 5 # вправо 5
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 5
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 5
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 6 # вправо 6
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 6
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 6
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 7 # вправо 7
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 7
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 7
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    return v

# *************************************************************************
def turn_king(v, n, i, j, f):
# король
    s = 'king'
    i_t = i - 1
    if i_t >= 0:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i
    j_t = j - 1
    if j_t >= 0:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    j_t = j + 1
    if j_t < 8:
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
    i_t = i + 1
    if i_t < 8:
        j_t = j
        v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j - 1
        if j_t >= 0:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
        j_t = j + 1
        if j_t < 8:
            v = ut.fish_go_ver_list(v, n, i, j, i_t, j_t, f)
# рокировка добавить
    return v

# *************************************************************************
def turn(v, n, x, y, desk):
    s = ' ku- ku '
    for i in range(x):
        for j in range(y):
            m = desk[i, j, 1]
            if m == 1:
                f = desk[i, j, 0]
                if f == 1:
                    v = turn_pawn(v, n, i, j, f)
                elif f == 2:
                    v = turn_rook(v, n, i, j, f)
                elif f == 3:
                    v = turn_knight(v, n, i, j, f)
                elif f == 4:
                    v = turn_beshop(v, n, i, j, f)
                elif f == 5:
                    v = turn_queen(v, n, i, j, f)
                elif f == 6:
                    v = turn_king(v, n, i, j, f)
    return v
