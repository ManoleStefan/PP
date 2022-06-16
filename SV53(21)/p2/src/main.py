from threading import *
r = RLock()

def f(X:{},Y:{}):
    #global r
    r.acquire()
    i = 0
    for j in range(0,X.__len__()):
        X[j] *= Y[i]
        X[j] += Y[i+1]
        i = i+1
    print(X)
    r.release()

if __name__ == '__main__':
    X = {0:4,
         1:10,
         2:89,
         3:99}

    Y = {0:6,
         1:9,
         2:7,
         3:5,
         4:10}
    t1 = Thread(target=f,args=(X,Y))
    t2 = Thread(target=f,args=(X,Y))
    t3 = Thread(target=f,args=(X,Y))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()