from multiprocessing import *

def funct(q,num,val,name):
    while(q.empty() == False):
        if((int)(num.value) % 3 == val):
            cuvant = q.get()
            print(f"Procesul {name} a citit {cuvant}")
            num.value = num.value-1

if __name__ == '__main__':

    f = open("C:\\Users\\user\\Desktop\\Facultate\\An2\\AN II CTI\\Anul II Sem II\\PP\\Subiecte Practic PP\\rezolvari practic\\SV65(13)\\p2\\input.txt",'r')

    sir = f.read().split(" ")

    print(sir)
    q = Queue()

    for i in sir:
        q.put(i)

    num = Value('i',sir.__len__())

    p1 = Process(target=funct,args=(q,num,0,"P1"))
    p2 = Process(target=funct,args=(q,num,1,"P2"))
    p3 = Process(target=funct,args=(q,num,2,"P3"))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

