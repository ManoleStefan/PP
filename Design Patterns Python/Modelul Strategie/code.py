import time

def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i],seq[(i+1) % n]

SLOW = 3
LIMIT = 5
WARNING = 'nu este bine deoarece ai ales un algoritm lent :('
def allUniqueSort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    strStr = sorted(s)
    for (c1,c2) in pairs(strStr):
        if c1 == c2:
            return False
    return True

def allUniqueSet(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s) == len(s)) else False

def allUnique(word,strategy):
    return strategy(word)


WORD_IN_DESC = 'Introduceti un cuvant (papa pentru iesire) > '
STRAT_IN_DESC = 'Alegeti o strategie: [1] baza pe set , [2] sorteaza si imperecheaza > '
while True:
    word = None
    while not word:
        word = input(WORD_IN_DESC)
        if word == 'papa':
            print('pa!!')
            break
        strategy_picked = None
        strategies = {'1': allUniqueSet,'2':allUniqueSort}
        while strategy_picked in strategies.keys():
            strategy_picked = input(STRAT_IN_DESC)
            try:
                strategy = strategies[strategy_picked]
                result = allUnique(word,strategy)
                print(f'AllUnique({word}) : {result}')
            except KeyError as err:
                print(f'Selectia gresita! : {strategy_picked}')
