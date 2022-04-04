# coding: utf-8

import re

# some parts are taken from https://github.com/potassium-chloride/WordleSolver

def isThisSecretAvailable(testword,mask,secret):
    if len(mask) != len(secret) or len(testword)!=len(secret):
        return False
    dup = set(testword[i] for i in range(len(mask)) if mask[i]=='G' or mask[i]=='Y')
    for i in range(len(mask)):
        if mask[i]=='N' and testword[i]!=secret[i] and (testword[i] not in secret or testword[i] in dup):
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
    newwordlist.extend(open('en.txt').read().splitlines())
    p1 = re.compile(r'\w|\[\w\]|\(\w\)')
    p2 = re.compile(r'\w|\-\w|\=\w')
    for a in args:
        m = p1.findall(a) if '[' in a or '(' in a else p2.findall(a)
        testword = [c.strip('-=()[]') for c in m]
        mask = ['G' if '[' in c or '=' in c else 'Y' if '(' in c or '-' in c else 'N' for c in m]
        newwordlist = getAvailableWordsByMask(testword, mask, newwordlist)
        #print(testword, mask, newwordlist)
    return newwordlist[:50]

if __name__ == "__main__":
    test = lambda x: print(x, solve(*x.split()))
    test('(a)bout f(l)[a](s)(h) [s][h][a]l[l]') # shawl
    test('-about f-l=a-s-h =s=h=al=l') # shawl
    test('н(о)рк[а] гли(с)(т) музей') # стопа
    test('но(р)ка глист муз(е)й [д]ожд[ь]') # дверь
    test('но-р=к=а глист д-ра=к=а =рыб=к=а =ра=м=к=а') # рюмка
