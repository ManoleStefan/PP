import threading
import time

EXIT_FLAG = 0

class Firicel(threading.Thread):
    def __init__(self,thread_id,name,counter):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def print_time(self,thread_name,delay,counter):
        while counter:
            if EXIT_FLAG:
                exit()
            time.sleep(delay)
            print("%s : %s"%(thread_name,time.ctime(time.time())))
            counter -= 1

    def run(self):
        print("Sunt %s si am pornit."%self.name)
        self.print_time(self.name,self.counter,5)
        print("Sunt %s si am terminat."%self.name)


thread1 = Firicel(1,'Firul 1',1)
thread2 = Firicel(2,'Firul 2',2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("S-a terminat firul principal")



