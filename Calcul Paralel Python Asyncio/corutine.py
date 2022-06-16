import asyncio as asy
@asy.coroutine
def stare0_start():
    print("Start din S0\n")
    valoare_intrare = int(input("Valoare intrare in S0 = "))
    if valoare_intrare == 0:
        rezultat = yield from stare2(valoare_intrare)
    else:
        rezultat = yield from stare1(valoare_intrare)

@asy.coroutine
def stare1(valoare_tranzitie):
    valoare_iesire = 'stare S1 cu valoarea de intrare = %s\n'%valoare_tranzitie
    valoare_intrare = int(input("Valoare intrare in S1 = "))
    print("...S1 - calculez...")
    if valoare_intrare == 0:
        rezultat = yield from stare3(valoare_intrare)
    else:
        rezultat = yield from stare2(valoare_intrare)

    return valoare_iesire + 'apel stare S1 cu {}'.format(rezultat)

@asy.coroutine
def stare2(valoare_tranzitie):
    valoare_iesire = 'stare S2 cu valoarea de tranzitie = %s\n'%valoare_tranzitie
    valoare_intrare = int(input("Valoare intrare in S2 = "))
    print("...S2 - calculez..")
    if valoare_intrare == 0:
        rezultat = yield from stare1(valoare_intrare)
    else:
        rezultat = yield from stare3(valoare_intrare)

    return valoare_iesire + 'apel stare 2 cu %s'%rezultat

@asy.coroutine
def stare3(valoare_tranzitie):
    valoare_iesire = 'stare S2 cu valoarea de tranzitie = %s\n'%valoare_tranzitie
    valoare_intrare = int(input("Valoare intrare in S3 = "))
    print("...S3 - calculez..")
    if valoare_intrare == 0:
        rezultat = yield from stare1(valoare_intrare)
    else:
        rezultat = yield from stare4_stop(valoare_intrare)

    return valoare_iesire + 'apel stare 2 cu %s'%rezultat

@asy.coroutine
def stare4_stop(valoare_tranzitie):
    valoare_iesire = 'sfarsit stare valoarea de tranzitie = %s\n'%valoare_tranzitie
    print("...S4 - calculez..")
    print('...Oprire...')

    return valoare_iesire

if __name__ == "__main__":
    print("Executie FSM utilizand Asyncio si Corutine")
    bucla = asy.get_event_loop()
    bucla.run_until_complete(stare0_start())