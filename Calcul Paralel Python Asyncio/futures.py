import asyncio as asy

@asy.coroutine
def prima_corutina(future,numar):
    contor = 0
    for i in range(1,numar+1):
        contor += i
    yield from asy.sleep(1)
    future.set_result("In prima corutina calculez suma a {} numere = {}".format(numar,contor))

@asy.coroutine
def a_doua_corutina(future,numar):
    contor = 1
    for i in range(2,numar+1):
        contor *= i
    future.set_result("In a doua corutina calculez factorial({}) = {}".format(numar,contor))

def preiau_rezultatul(future):
    print(future.result())




if __name__ == "__main__":
    numar1 = int(input("Numarul 1 : "))
    numar2 = int(input("Numarul 2 : "))
    bucla = asy.get_event_loop()
    future1 = asy.Future()
    future2 = asy.Future()

    tasks = [prima_corutina(future1,numar1),a_doua_corutina(future2,numar2)]

    future1.add_done_callback(preiau_rezultatul)
    future2.add_done_callback(preiau_rezultatul)
    bucla.run_until_complete(asy.wait(tasks))
    bucla.close()