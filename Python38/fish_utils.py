# fish_utils
#  20.08.13 - файл функкций проекта fish
# *************************************************************************
def desk_gorisont_list(f):
# 20.08.13 - буква доски проекта fish
    s = ''
    if f == 0:
        s = 'a'
    elif f == 1:
        s = 'b'
    elif f == 2:
        s = 'c'
    elif f == 3:
        s = 'd'
    elif f == 4:
        s = 'e'
    elif f == 5:
        s = 'f'
    elif f == 6:
        s = 'g'
    elif f == 7:
        s = 'h'
    else:
        s = 'X'
        print('fish_gorisont_list: ошибка. вне доски', f)
    return s

# *************************************************************************
def desk_vertikal_list(f):
# 20.08.13 - цифра доски проекта fish
    if f >= 0 and f <= 7:
        s = str(f + 1)
    else:
        s = 'X'
        print('fish_vernikal_list: ошибка. вне доски', f)
    return s

# *************************************************************************
def desk_position_list(i, j):
# 20.08.13 - клетка доски проекта fish
    s = desk_gorisont_list(i)
    s += desk_vertikal_list(j)
    return s

# *************************************************************************
def desk_fig_position_list(i, j, f):
# 20.08.13 - фигура на клетке доски проекта fish
    s = fish_figure_list(f) + ' '
    s += desk_gorisont_list(i)
    s += desk_vertikal_list(j)
    return s

# *************************************************************************
def fish_figure_list(f):
#  20.08.13 - название фигуры проекта fish
    s = ''
    if f == 1:
        s=''
    elif f == 2:
        s = 'Л'
    elif f == 3:
        s ='К'
    elif f == 4:
        s = 'С'
    elif f == 5:
        s = 'Ф'
    elif f == 6:
        s = 'Кр'
    else:
        s = 'X'
        print('fish_position_list: ошибка. неопознанная фигура', f)
    return s

# *************************************************************************
def fish_go_list(n, i, j, i_t, j_t, f):
# 20.08.13 - клетка доски проекта fish
    s = str(n) + '. '
    s += desk_fig_position_list(i, j, f) + ' - '
    s += desk_position_list(i_t, j_t)
    return s

# *************************************************************************
def fish_go_ver_list(v, n, i, j, i_t, j_t, f):
# 20.08.13 - ход проекта fish
    v += 1
    s1 = str(v)
    print('{:>8}'.format(s1), end='')
    print(' : ', end='')
    if f <= 6:
        s = fish_go_list(n, i, j, i_t, j_t, f)
        print(s)
    elif f == 7:
        s = str(n) + '. 0 - 0'
        print(s)
    elif f == 8:
        s = str(n) + '. 0 - 0 - 0'
        print(s)
    elif f == 9:
        s = fish_go_list(n, i, j, i_t, j_t, 1)
        print(s, end='')
        print('Ф')
        v += 1
        s1 = str(v)
        print('{:>8}'.format(s1), end='')
        print(' :  ', end='')
        print(s, end='')
        print('К')
        v += 1
        s1 = str(v)
        print('{:>8}'.format(s1), end='')
        print(' : ', end='')
        print(s, end='')
        print('С')
        v += 1
        s1 = str(v)
        print('{:>8}'.format(s1), end='')
        print(' : ', end='')
        print(s, end='')
        print('Л')

# рокировка
# пешка перевертыш добавить
    return v

# *************************************************************************
def fish_position_list(x, y, desk):
# 20.08.13 - ход проекта fish
    sw = 'Белые  : '
    sb = 'Черные : '

    for i in range(x):
        for j in range(y):
            f = desk[i, j, 1]
            if f != 0:
                s = desk_fig_position_list(i, j, desk[i, j, 0])+', '
                if f == 1:
                    sw += s
                elif f == 2:
                    sb += s
                else:
                    print('fish_nu: ошибка. неопознанный цвет', f)
    print(sw)
    print(sb)
    return sw, sb
