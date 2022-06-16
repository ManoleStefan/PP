import multiprocessing
import os

q = multiprocessing.Queue()
procese = []
lista = []
def proc_pid(n):
    q.put(os.getpid())
    print("\n[{}] Salut !".format(n))

for i in range(5):
    t = multiprocessing.Process(target=proc_pid,args=(i,))
    procese.append(t)
    t.start()

for un_proces in procese:
    print(un_proces.name)
    un_proces.join()

while not q.empty():
    lista.append(q.get())

print(lista," de lungime ",len(lista))