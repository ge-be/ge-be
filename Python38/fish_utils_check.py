# fish_utils_check
# проверка на шах - 20.08.14 - 20.08.15

def king_black(x, y, desk):
# позиция черного короля
    ikb = 15
    jkb = 15
    for i in range(x):
        for j in range(y):
            m = desk[i, j, 1]
            if m == 2:
                f = desk[i, j, 0]
                if f == 6:
                    ikb = i
                    jkb = j
    if ikb == 15 or jkb == 15:
        print('черный король вне доски')
    return ikb, jkb

# *************************************************************************
def king_white(x, y, desk):
# позиция белого короля
    ikw = 15
    jkw = 15
    for i in range(x):
        for j in range(y):
            m = desk[i, j, 1]
            if m == 1:
                f = desk[i, j, 0]
                if f == 6:
                    ikw = i
                    jkw = j
    if ikw == 15 or jkw == 15:
        print('белый король вне доски')
    return ikw, jkw

# *************************************************************************
def king_check(c, x, y, ikw, jkw, desk):
# угроза  королю
# пешки
    f = 1
    if c == 2:
# белому
        j = jkw + 1
        if j < y - 1:
            i = ikw + 1
            if i < x:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
            i = ikw - 1
            if i >= 0:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
    elif c == 1:
# черному
        j = jkw - 1
        if j > 0:
            i = ikw + 1
            if i < x:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
            i = ikw - 1
            if i >= 0:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
# ладья
    f = 2
    i = ikw
    j = jkw + 1
    if j < y:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    j = jkw + 2
    if jkw < y:
        for j in range(jkw + 2, y):
            b = False
            for j1 in range(jkw + 1, j - 1):
                if desk[i, j1, 1] != 0:
                    b = True
                    break
            if b:
                break
            else:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
    j = jkw - 1
    if j >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    j = jkw - 2
    if j >= 0:
        for j in range(jkw - 1):
            b = False
            for j1 in range(j + 1, jkw - 1):
                if desk[i, j1, 1] != 0:
                    b = True
                    break
            if b:
                break
            else:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
    i = ikw + 1
    j = jkw
    if i < x:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    i = ikw + 2
    if i < x:
        for i in range(ikw + 2, x):
            b = False
            for i1 in range(ikw + 1, i):
                if desk[i1, j, 1] != 0:
                    b = True
                    break
            if b:
                break
            else:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
    i = ikw - 1
    if i >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    i = ikw - 2
    if i >= 0:
        for i in range(ikw - 1):
            b = False
            for i1 in range(i + 1, ikw - 1):
                print(i, i1, j)
                if desk[i1, j, 1] != 0:
                    b = True
                    break
            if b:
                break
            else:
               if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
# конь
    f = 3
    j = jkw + 1
    if j < y:
        i = ikw + 2
        if i < x:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
        i = ikw - 2
        if i >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
               return f, i, j
    j = jkw + 2
    if j < y:
        i = ikw + 1
        if i < x:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
        i = ikw - 1
        if i >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    j = jkw - 1
    if j >= 0:
        i = ikw + 2
        if i < x:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
        i = ikw - 2
        if i >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    j = jkw - 2
    if j >= 0:
        i = ikw + 1
        if i < x:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
        i = ikw - 1
        if i >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
# слон
    f = 4
    i = ikw + 1
    if i < x:
        j = jkw + 1
        if j < y:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw + 2
    if i < x:
        j = jkw + 2
        if j < y:
            for j in range(jkw + 2, y):
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i - 1, j - 1, 1] != 0:
                    break
                i += 1
                if i >= x:
                    break
    i = ikw + 1
    if i < x:
        j = jkw - 1
        if j >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw + 2
    if i < x:
        j = jkw - 2
        if j >= 0:
            while j >= 0:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i - 1, j + 1, 1] != 0:
                    break
                i += 1
                if i >= x:
                    break
    i = ikw - 1
    if i >= 0:
        j = jkw + 1
        if j < y:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw - 2
    if i >= 0:
        j = jkw + 2
        if j < y:
            for j in range(jkw + 2, y):
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i + 1, j - 1, 1] != 0:
                    break
                i -= 1
                if i <= 0:
                    break
    i = ikw - 1
    if i >= 0:
        j = jkw - 1
        if j >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw - 2
    if i >= 0:
        j = jkw - 2
        if j >= 0:
            while j >= 0:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i + 1, j + 1, 1] != 0:
                    break
                i -= 1
                if i < 0:
                    break
# ферзь
    f = 5
    i = ikw
    j = jkw + 1
    if j < y:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    j = jkw + 2
    if j < y:
        for j in range(jkw + 2, y):
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
            if desk[i, j - 1, 1] != 0:
                break
    j = jkw - 1
    if j >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    j = jkw - 2
    if j >= 0:
        while i >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
            if desk[i, j - 1, 1] != 0:
                break
            i -= 1
    i = ikw + 1
    j = jkw
    if i < x:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return i, j
    i = ikw + 2
    if i < x:
        for i in range(ikw + 2, x):
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
            if desk[i, j - 1, 1] != 0:
                break
    i = ikw - 1
    if i >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    i = ikw - 2
    if i >= 0:
        while i >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
            if desk[i, j - 1, 1] != 0:
                break
            i -= 1
    i = ikw + 1
    if i < x:
        j = jkw + 1
        if j < y:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw + 2
    if i < x:
        j = jkw + 2
        if j < y:
            for j in range(jkw + 2, y):
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i - 1, j - 1, 1] != 0:
                    break
                i += 1
                if i >= x:
                    break
    i = ikw + 1
    if i < x:
        j = jkw - 1
        if j >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw + 2
    if i < x:
        j = jkw - 2
        if j >= 0:
            while j >= 0:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i - 1, j + 1, 1] != 0:
                    break
                i += 1
                if i >= x:
                    break
    i = ikw - 1
    if i >= 0:
        j = jkw + 1
        if j < y:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw - 2
    if i >= 0:
        j = jkw + 2
        if j < y:
            for j in range(jkw + 2, y):
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i + 1, j - 1, 1] != 0:
                    break
                i -= 1
                if i <= 0:
                    break
    i = ikw - 1
    if i >= 0:
        j = jkw - 1
        if j >= 0:
            if desk[i, j, 1] == c and desk[i, j, 0] == f:
                return f, i, j
    i = ikw - 2
    if i >= 0:
        j = jkw - 2
        if j >= 0:
            while j >= 0:
                if desk[i, j, 1] == c and desk[i, j, 0] == f:
                    return f, i, j
                if desk[i + 1, j + 1, 1] != 0:
                    break
                i -= 1
                if i < 0:
                    break
# король
    f = 6
    i = ikw
    j = jkw + 1
    print('c = ', c, ' f = ', f, ' i = ', i, ' j = ', j)
    if j < y:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    i = ikw + 1
    if i < x and j < y:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    j = jkw
    if desk[i, j, 1] == c and desk[i, j, 0] == f:
        return f, i, j
    j = jkw - 1
    if i < x and j >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    i = ikw
    if j >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    i = ikw - 1
    if i >= 0 and j >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    j = jkw
    if i >= 0:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j
    j = jkw + 1
    if i >= 0 and j < y:
        if desk[i, j, 1] == c and desk[i, j, 0] == f:
            return f, i, j

    i = x + 1
    j = y + 1
    f = 15
    return f, i, j

# *************************************************************************
def test_king(x, y, desk):
    ''' проверка на количество королей на доске '''
    kb = 0
    kw = 0
    for i in range(x):
        for j in range(y):
            if desk[i, j, 0] == 6:
                if desk[i, j, 1] == 1:
                    kw += 1
                elif desk[i, j, 1] == 2:
                    kb += 1
    return kw, kb