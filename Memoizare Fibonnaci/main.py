import time
import threading

def Fibbo(n):
    def Fibbonaci(n):
        if n == 1 or n == 2:
            return 1
        return Fibbonaci(n-1) + Fibbonaci(n-2)

    start = time.time()
    print(Fibbonaci(n))
    end = time.time()
    print("Executie Fibbonaci(100) fara memoizare : {}".format(end-start))

def FibboM(n,memo):
    def FibbonaciMemo(n,memo):
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = FibbonaciMemo(n-1,memo) + FibbonaciMemo(n-2,memo)
            return memo[n]

    start = time.time()
    print(FibbonaciMemo(n,memo))
    end = time.time()
    print("Executie Fibbonaci(100) cu memoizare : {}".format(end-start))

memo = [0] * 101
memo[1] = memo[2] = 1

thread1 = threading.Thread(target = Fibbo,args=(100,))
thread2 = threading.Thread(target = FibboM,args=(100,memo))
thread1.start()
thread2.start()