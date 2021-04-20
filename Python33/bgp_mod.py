''' 
bgp_mod.py - модуль с функциями
Created on 2013.11.21
@author: bgp

dic(d, fo)             - 2, 3 составление словаря файла 
dic_db(d)              - 2, 3 перенос словаря в базу 
dic_fl(d, f)           - 2, 3 словарь в файл ms_fl(d, f)
dic_sud(d)             - 2, 3 сорторовка и удаление элементов с 0 из словаря
excp()                 - 2, 3 exceptions исключения
fib()                  - 3 !! фибоначи
glp()                  - 2, 3 глобальные переменные пути
glv()                  - удален 3 !! глобальные переменные режима
gls()                  - 2, 3 глобальные переменные sql, протоколы
prt2()                 - 3 !!  печать 2 значения
prot_finish(m, c = '') - 2, 3 запись в протокол о конце процедуры
prot_start(m, c = '')  - 2, 3 запись в протокол о начале процедуры
prot_wr(m, op, c = '') - 2, 3 запись в протокол 
punc()                 - 2, 3 punctuation marks знаки пунктуации
table_cr(m, s[1], fl)  - 2, 3 создание таблицы
table_oc()             - 2, 3 создание таблицы оценок
table_ocv()            - 2, 3 создание таблицы оценок вектора
table_prt()            - 2, 3 создание таблицы протокола
table_ud(m, tn, r = 0) - 2, 3 удаление таблицы
vec(fo, fr, d)         - 2, 3 вектор файла
walk(p, d)             - 2, 3 прогулка по каталогу для создания словаря
walkt(mt, p, r, d)     - 2, 3 прогулка по каталогу для формирования вектора
fn[]
    import pdb
'''
    
# составление словаря файла 2, 3
def dic(d, fo): 
    g = gls()
    s = g.f()
    f1 = open(fo, 'r')
    if s[3] == 2:
        import bgp2mod
        fz   = bgp2mod.punc()
        fe   = bgp2mod.excp()
    else:
        import bgp_mod
        fz   = bgp_mod.punc()
        fe   = bgp_mod.excp()

    w  = ""
    wo = ""
    for k in f1.read():
        if k not in fz:
            w = w + k
        else:
            if w:
                w = w.lower() # строчные буквы
                if w in fe:
                    wo = ""
                    w  = ""
                    continue
                if w in d:
                    d[w] += 1
                else:
                    d[w] = 1
                if wo: 
                    w1 = wo + " " + w
                    if w1 in d:
                        d[w1] += 1
                    else:
                        d[w1] = 1
                if k == " ":
                    wo = w
                else:    
                    wo = ""
            w  = ""
    f1.close()
    return d

# перенос словаря в базу  2, 3
def dic_db(d): 
    g = gls()
    s = g.f()
    m = 'dic_db'
    if s[7] == 1: tn = 'bgp_dic_t'
    else:         tn = 'bgp_dic_w'
    fl = 'key text, val real'
    if s[3] == 2:
        import bgp2mod
        f    = bgp2mod.table_ud(m, tn, 1)
        f    = bgp2mod.table_cr(m, tn, fl)
        import sqlite
        con  = sqlite.connect(s[0])#создаём соединение с базой данных
    else:    
        import bgp_mod
        f    = bgp_mod.table_ud(m, tn, 1)
        f    = bgp_mod.table_cr(m, tn, fl)
        import sqlite3
        con  = sqlite3.connect(s[0])#создаём соединение с базой данных
    cur = con.cursor()#создаём курсор - основной инструмент работы с БД
    for k in d:
        cur.execute('insert into ' + tn + ' (key,  val) values (?, ?)',
                    (k, d[k]))
    con.commit()#сохраняем изменения
    con.close()
    return 1

# словарь в файл ms_fl(d, f) 2, 3
def dic_fl(d, f):
    f2 = open(f, 'w')
    for i in d:
        f2.write(i + ' : ' + str(d[i]) +'\n')
    f2.close()
    return 1
    
#  dr = bgp_mod.dic_nrm(dr) # нормировка словаря 2, 3
def dic_nrm(d):
    dw = {}
    for i in d:
        if d[i] > 0:  dw[i] = 1
        else: dw[i] = -1
    return dw

# сорторовка и удаление элементов с 0 из словаря 2, 3
def dic_sud(d):
    dw = {}
    for i in sorted(d):
        if d[i] != 0:
            dw[i] = d[i]
    return dw

# exceptions исключения 2, 3
def excp():
    ex = ("a","an","it","with","on","but","of","by","and","or","the","is","to","also","in","as",
          "at","mr","ms","so","about","after",) # кортеж-неизменимый список знаков
    return ex

# фибоначи 3 !!!
def fib(n): 
    a = b = 1
    for i in range(n):
        a, b = b, a + b
        print (i, a, b)
    return b

# глобальные переменные пути 2, 3
def glp():
    import os
    
    pathb = os.path.dirname(os.path.abspath(__file__)) # C:\Python33\bgp_py
    path  = os.path.join(os.path.dirname(pathb), 'WEB')# C:\Python33\WEB
    patht = os.path.join(path,  'TEST')                # C:\Python33\WEB\TEST
    pathi = os.path.join(path,  'in')                  # C:\Python33\WEB\in
    patho = os.path.join(path,  'train')               # C:\Python33\WEB\train
    pathn = os.path.join(patho, 'neg')                 # C:\Python33\WEB\train\neg
    pathp = os.path.join(patho, 'pos')                 # C:\Python33\WEB\train\pos
    pathr = os.path.join(patho, 'rez')                 # C:\Python33\WEB\train\res
    pattp = os.path.join(patht, 'pos')                 # C:\Python33\WEB\TEST\pos
    pattn = os.path.join(patht, 'neg')                 # C:\Python33\WEB\TEST\neg
    pattr = os.path.join(patht, 'rez')                 # C:\Python33\WEB\TEST\res
    patti = os.path.join(patht, 'in')                 # C:\Python33\WEB\TEST\in
#             0      1     2      3      4      5
    return (pathb, path, patht, pathi, pathp, pathn, 
#             6      7     8      9       10
            pathr, pattp, pattn, pattr, patti,)

# глобальные переменные, sql, протоколы 2, 3
class gls(): 
    def __init__(self):
        self.pv = 3              # 2 - версия Python2  или любой
        self.mt = 1              # 1 - среднее арифметическое, 2 - SVM
        self.r  = 0              # 1 - быстрый тест или 0 - полный
        self.pt = 0              # 1 - файл  или 0 - протокол таблица
        self.fp = 'bgp_log'      # - имя протокола таблица 
        self.fl = 'bgp_log.txt'  # - имя протокола файл
        if self.pv == 2:
            self.sq = 'sqlite'   # - имя модуля базы
            self.bm = 'bgp2mod'  # - имя модуля
        else:
            self.sq = 'sqlite3'  # - имя модуля базы 
            self.bm = 'bgp_mod'  # - имя модуля
        self.b  = 'bgp.' + self.sq   # - имя базы sql
#                   0        1        2        3        4         
        self.s = (self.b, self.fp, self.fl, self.pv, self.sq,
#                   5        6        7        8        9        10  
                  self.bm, self.mt, self.r, self.pt,)
    def f(self):
        return self.s

# глобальные переменные режима
'''
def glv():
#    global mt, R, pt
    mt = 1  # метод : 1 среднее арифметическое, 2 - SVM
    R  = 1  # 1 - быстрый тест, 0 - полный
    pt = 1  # 0 - протокол таблица, 1 - файл
#    ver= 3  # 2 -версия питона
#           0   1   2   3  
    return (mt, R, pt)
'''

# печать 2 значения 3 !!!
def prt2(nm, val):
    g = gls()
    s = g.f()
    if s[3] == 2:
        a = 1
#        print nm, val
    else:
        a = 1
        print (nm, val)        
    
# запись в протокол о начале процедуры 2, 3
def prot_start(m, c = ''): 
    g = gls()
    s = g.f()
    op = 'Start '
    if s[3] == 2:
        import bgp2mod
        f    = bgp2mod.prot_wr(m, op, c)
    else:
        import bgp_mod
        f    = bgp_mod.prot_wr(m, op, c)
    return 1

# запись в протокол о конце процедуры 2, 3
def prot_finish(m, c = ''): 
    g = gls()
    s = g.f()
    op = 'Finish'
    if s[3] == 2:
        import bgp2mod
        f    = bgp2mod.prot_wr(m, op, c)
    else:
        import bgp_mod
        f    = bgp_mod.prot_wr(m, op, c)
    return 1

# запись в протокол 2, 3
def prot_wr(m, op, c = ''): 
    import datetime

    g = gls()
    s = g.f()
    
    now_time = datetime.datetime.now() # Текущая дата с
    d_t = (now_time.strftime("%y.%m.%d %H:%M:%S"))
#    print ( m, op, d_t, c, ' R = ' + str(s[8])
    if s[8] == 1:
        import os
        if s[3] == 2:
            import bgp2mod
            p    = bgp2mod.glp()
        else:
            import bgp_mod
            p    = bgp_mod.glp()
        fw = os.path.join(p[1], s[2])
        f2 = open(fw, 'a')
        f2.write(m + ', ' + op + ', ' +  d_t + ', ' + c + ' \n')
        f2.close()
    else:
        if s[3] == 2:
            import sqlite
            con  = sqlite.connect(s[0]) #создаём соединение с базой данных
        else:
            import sqlite3
            con  = sqlite3.connect(s[0]) #создаём соединение с базой данных
#        con.row_factory = sqlite3.Row
        cur = con.cursor() #создаём курсор - основной инструмент работы с БД
        cur.execute('insert into ' + s[1] + ' (name, oper, date_time, comment) values (?, ?, ?, ?)',
                                              (m, op, d_t, c))
        con.commit() #сохраняем изменения
        con.close()    
    return 1

# punctuation marks знаки пунктуации 2, 3
def punc():
    pm = (" ","'","`",'"',"#","•","","","\n","/n",",","/",".","!","?",";",":","-",")","(","*","^","$","|","=","%",
          "<",">","_","@","&","+","[","]","{","}","0","1","2","3","4","5","6","7","8","9","~",) # кортеж-неизменимый список знаков
    return pm

#f = bgp_mod.table_cr(m, tn, fl)# создание таблицы 2, 3
def table_cr(m, tn, fl):
    g = gls()
    s = g.f()
    if s[3] == 2:
        import sqlite
        con  = sqlite.connect(s[0]) #создаём соединение с базой данных
    else:
        import sqlite3
        con  = sqlite3.connect(s[0]) #создаём соединение с базой данных
    mm = 'table_cr'
    cur = con.cursor() #создаём курсор - основной инструмент работы с БД
    cur.execute('create table if not exists ' + tn + ' (' + fl + ')') 
    con.commit() #сохраняем изменения
    con.close()
    op = " table created "
    if s[3] == 2:
        import bgp2mod
        bgp2mod.prot_wr(m, mm, op + tn )
    else:
        import bgp_mod
        bgp_mod.prot_wr(m, mm, op + tn )
    return 1
  
#f = bgp_mod.table_oc()# создание таблицы оценок 2, 3
def table_oc(m):
    g = gls()
    s = g.f()
    nm = "bgp_oc"    
    fl = 'name text, qty integer, val integer, r real, rez text'
    if s[3] == 2:
        import bgp2mod
        f = bgp2mod.table_ud(m, nm, 1)
        f = bgp2mod.table_cr(m, nm, fl)# создание таблицы
    else:
        import bgp_mod
        f = bgp_mod.table_ud(m, nm, 1)
        f = bgp_mod.table_cr(m, nm, fl)# создание таблицы
    return 1
        
#f = bgp_mod.table_ocv()# создание таблицы оценок вектора 2, 3
def table_ocv(m):
    g = gls()
    s = g.f()
    nm = "bgp_ocv"  
    fl = 'name text, key text, val integer'
    if s[3] == 2:
        import bgp2mod
        f = bgp2mod.table_ud(m, nm, 1)
        f = bgp2mod.table_cr(m, nm, fl)# создание таблицы
    else:
        import bgp_mod
        f = bgp_mod.table_ud(m, nm, 1)
        f = bgp_mod.table_cr(m, nm, fl)# создание таблицы
    return 1
        
#f = bgp_mod.table_prt()# создание таблицы оценок 2, 3
def table_prt(m):
    g = gls()
    s = g.f()
    nm = "bgp_log"    
    fl = 'name text(10), oper text(5), data time text(17), comment text(50)'
    if s[3] == 2:
        import bgp2mod
        f    = bgp2mod.table_ud(m, nm, 0)
        f    = bgp2mod.table_cr(m, nm, fl)# создание таблицы
    else:
        import bgp_mod
        f    = bgp_mod.table_ud(m, nm, 0)
        f    = bgp_mod.table_cr(m, nm, fl)# создание таблицы
    return 1
    
# удаление таблицы 2, 3
def table_ud(m, tn, r = 0):
    g = gls()    
    s = g.f()
    mm = 'table_ud'
    if r == 1:
        if s[3] == 2:
            import sqlite
            con  = sqlite.connect(s[0]) #создаём соединение с базой данных
        else:        
            import sqlite3
            con  = sqlite3.connect(s[0]) #создаём соединение с базой данных
        cur = con.cursor() #создаём курсор - основной инструмент работы с БД
        cur.execute('drop table if exists  ' + tn )#удаляем таблицу
        con.commit() #сохраняем изменения
        con.close()
        op = 'удалена таблица '
        if s[3] == 2:
            import bgp2mod
            f  = bgp2mod.prot_wr(m, mm, op + tn )
        else:
            import bgp_mod
            f  = bgp_mod.prot_wr(m, mm, op + tn )
        return 1
    else:
        op = 'HE удалена таблица '
        if s[3] == 2:
            import bgp2mod
            f  = bgp2mod.prot_wr(m, mm , op + tn)
        else:
            import bgp_mod
            f  = bgp_mod.prot_wr(m, mm , op + tn)
        return 0

 # вектор файла 2, 3
def vec(fo, fr, d): 
    g = gls()    
    s = g.f()
    nm= 'vec'
    f1 = open(fo, 'r')
    import os
    if s[3] == 2:
        import bgp2mod
        import sqlite
        fz = bgp2mod.punc()
        fe = bgp2mod.excp()
    else:
        import bgp_mod
        import sqlite3
        fz = bgp_mod.punc()
        fe = bgp_mod.excp()
    w  = ""
    wo = ""
    dt = {}
    for k in f1.read():
        if k not in fz:
            w = w + k
        else:
            if w:
                w = w.lower() # строчные буквы
                if w in fe:
                    wo = ""
                    w  = ""
                    continue
                if w in d:
                    dt[w] = d[w]
                else:
                    dt[w] = 0
                if wo: 
                    w1 = wo + " " + w
                    if w1 in d:
                        dt[w1] = d[w1]
                    else:
                        dt[w1] = 0
                if k == " ":
                    wo = w
                else:    
                    wo = ""
            w  = ""
    f1.close()
    dt = bgp_mod.dic_sud(dt)    
    f2 = open(fr, 'w')
    tn = "bgp_ocv"    
    tr = "bgp_oc"    
    if s[3] == 2:
        con = sqlite.connect(s[0])#создаём соединение с базой данных
    else:
        con = sqlite3.connect(s[0])#создаём соединение с базой данных
    cur = con.cursor()#создаём курсор - основной инструмент работы с БД
    sm = 0    
    q  = 0
    fn =  os.path.split(fr)
    for i in dt:
        sm += dt[i]
        q  += 1
        f2.write(i + ' : ' + str(dt[i]) +'\n')
        if dt[i] != 0: 
            cur.execute('insert into ' + tn +
             ' (name, key,  val) values (?, ?, ?)', (fn[1], i, d[i]))
#    print ('q = ', q, 'sm =', sm)    
    con.commit()#сохраняем изменения
    con.close()
    f2.close()
    if s[6] == 1: r = sm / q
    else:         r = 0.3
    mx =  0.15
    mn = -0.025
    if r > mx:           re = 'pos'
    elif mn <= r <= mx:  re = 'net'
    else:                re = 'neg'
    if s[3] == 2:
        f  = bgp2mod.prot_wr(' ', nm , fn[1] + ' ' + str(r))
    else:
        f  = bgp_mod.prot_wr(' ', nm , fn[1] + ' ' + str(r))
  
    con = sqlite3.connect(s[0])#создаём соединение с базой данных
    cur = con.cursor()#создаём курсор - основной инструмент работы с БД
 
    cur.execute('insert into ' + tr + ' (name, qty,  val, r, rez) values (?, ?, ?, ?, ?)',
                                        (fn[1], q, sm, r, re))  
    con.commit()#сохраняем изменения
    con.close()
    return 1

# прогулка по каталогу для создания словаря 2, 3
def walk(p, d):
    g = gls()    
    s = g.f()
    import os
    if s[3] == 2:
        import bgp2mod
    else:
        import bgp_mod    
    n = 0
    for name in os.listdir(p):
        fo = os.path.join(p, name)
        if os.path.isfile(fo):
            n += 1
            if s[3] == 2:
                d = bgp2mod.dic(d, fo)
            else:
                d = bgp_mod.dic(d, fo)
        else:
            walk(fo)
    return d        

#    f = bgp_mod.vec_f(fo, fr, d)# - оценки в файл 2, 3
def vec_f(p, r, d):
    return 1

# прогулка по каталогу для оценки тональности файлов
def walkt(p, r, d):
    import bgp_mod
    import os
#    import pdb
    
    m = 'walk_t'
    f  = bgp_mod.table_ocv(m)# создание таблицы оценок вектора
    f  = bgp_mod.table_oc(m)# создание таблицы оценок 
    n = 0
    p1 =  os.path.join(p, 'pos')
    p2 =  os.path.join(p, 'neg')
    print('p1 = ', p1)
    print('p2 = ', p2)
    for name in os.listdir(p1):
        fo = os.path.join(p1, name)
        fr = os.path.join(r, 'p' + name)
        if os.path.isfile(fo):
            n += 1
            f = bgp_mod.vec(fo, fr, d)
    print('n  = ', n)
    for name in os.listdir(p2):
        fo = os.path.join(p2, name)
        fr = os.path.join(r, 'n' + name)
        if os.path.isfile(fo):
            n += 1
            f = bgp_mod.vec(fo, fr, d)
    print('n  = ', n)
    return 1 

# тональная оценка файла

m = 'bgp_mod'
print(m, " : Mistakes isn't revealed.")    

