import multiprocessing
import time
from queue import Queue


class Proces(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                print('%s: terminat' % proc_name)
                self.task_queue.task_done()
                break
            print('%s: %s' % (proc_name, next_task))
            next_task()
            self.task_queue.task_done()
        return


class Task(object):
    def __init__(self, a):
        self.a = a

    def __call__(self):
        time.sleep(0.1)
        return 'procesul a returnat cuvantul %a' % self.a

    def __str__(self):
        return 'returnez cuvantul %a' % self.a


if __name__ == '__main__':
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    nrProcese = 3
    procese = [Proces(tasks, results) for i in range(nrProcese)]
    for w in procese:
        w.start()

    coada = Queue()
    coada.put("Cuvant1")
    coada.put("Cuvant2")
    coada.put("Cuvant3")
    coada.put("Cuvant4")
    coada.put("Cuvant5")
    while coada.qsize() != 0:
        tasks.put(Task(coada.get()))

    for i in range(nrProcese):
        tasks.put(None)

    tasks.join()
