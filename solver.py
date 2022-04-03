# coding: utf-8

import re

# some parts are taken from https://github.com/potassium-chloride/WordleSolver

def isThisSecretAvailable(testword,mask,secret):
    if len(mask) != len(secret) or len(testword)!=len(secret):
        return False
    dup = set(testword[i] for i in range(len(mask)) if mask[i]=='G' or mask[i]=='Y')
    for i in range(len(mask)):
        if mask[i]=='N' and (testword[i] not in secret or testword[i] in dup):
            continue
        if mask[i]=='G' and testword[i]==secret[i]:
            continue
        if mask[i]=='Y' and testword[i] in secret and testword[i]!=secret[i]:
            continue
        return False
    return True

def getAvailableWordsByMask(testword,mask,wordlist):
    validsecrets=[]
    for w in wordlist:
        if(isThisSecretAvailable(testword,mask,w)):
            validsecrets.append(w)
    return validsecrets

def solve(*args):
    newwordlist = open('ru.txt', encoding='utf-8').read().splitlines()
    newwordlist.extend(open('en.txt', encoding='utf-8').read().splitlines())

    p = re.compile(r'\w|\[\w\]|\(\w\)')
    for a in args:
        m = p.findall(a)
        testword = [c.strip('[]()') for c in m]
        mask = ['G' if '[' in c else 'Y' if '(' in c else 'N' for c in m]
        newwordlist = getAvailableWordsByMask(testword, mask, newwordlist)
        #print(testword, mask, newwordlist)
    return newwordlist[:50]

if __name__ == "__main__":
    test = lambda x: print(x, solve(*x.split()))
    test('н(о)рк[а] гли(с)(т) музей') # стопа
    test('но(р)ка г[л]ист муз[е]й') # плеер
    test('нор[к][а] гли(с)т фа(с)[к][а]') # сушка
    test('но(р)ка глист муз(е)й [д]ожд[ь]') # дверь
    test('(a)dieu [s](w)eet [s]p[a][w]s [s][h][a][w]n') # shawm shaws


