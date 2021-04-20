#!/usr/bin/env python
# -*- coding: utf-8 -*-

m = "bgp2004" #.py - старт для проекта WEB
'''
Created on 2013.11.21
author: bgp
'''
import bgp2mod
import os
import pdb

print ' S T A R T ********* ', m 
#pdb.set_trace()
print "m = ", m
f  = bgp2mod.prot_start(m)

g = bgp2mod.gls()
s = g.f()
p = bgp2mod.glp()
#pdb.set_trace()
op = "R= " + str(s[7])+', V= ' + str(s[3])
print "m = ", m, 'op = ', op
f = bgp2mod.prot_wr(m, "", op)
if s[7] == 1:  # R = 1 - быстрый тест,
    fp = 'tsbgp_00105.txt' # словарь позитивный
    fn = 'tsbgp_00106.txt' # словарь негативный
    fr = 'tsbgp_00108.txt' # словарь сводный
    pp = p[7]
    pn = p[8]
    pr = p[9]
    pv = p[10]
else: # R <> 1  0 - полный словарь
    fp = 'tsbgp_00103.txt' # словарь позитивный
    fn = 'tsbgp_00104.txt' # словарь негативный
    fr = 'tsbgp_00107.txt' # словарь сводный
    pv = p[3]
    pp = p[4]
    pn = p[5]
    pr = p[6]

dp = {}
dp = bgp2mod.walk(pp, dp)
ff = os.path.join(pr, fp)
print 'pozitiv = ', ff
f = bgp2mod.dic_fl(dp, ff) # словарь в файл

dn = {}
dn = bgp2mod.walk(pn, dn)
ff = os.path.join(pr, fn)
print 'negativ = ', ff
f = bgp2mod.dic_fl(dn, ff) # словарь в  файл

dr = {}
ff =  os.path.join(pr, fr)
print 'all = ', ff

for i in dp:
    dr[i] = dp[i]
for i in dn:
    if i in dr:
        dr[i] = dr[i] - dn[i]
    else:
        dr[i] = 0 - dn[i]

dn = {}
dp = {}
dr = bgp2mod.dic_sud(dr) # сорторовка и удаление элементов с 0 из словаря
dr = bgp2mod.dic_nrm(dr) # нормировка словаря
f  = bgp2mod.dic_fl(dr, ff) # словарь в файл
f  = bgp2mod.dic_db(dr) # словарь в таблицу /  обработка словаря
f  = bgp2mod.prot_wr(m, str(s[3]), pv + ' - ' + pr)
f  = bgp2mod.walkt(pv, pr, dr) # оценка новых файлов
f  = bgp2mod.prot_finish(m)

print ' F I N I S H  ********* ', m 

