import multiprocessing

class ProcessTest(multiprocessing.Process):
    def run(self):
        print("Am apelat metoda run() in procesul {}".format(self.name))
        return

if __name__ == "__main__":
    jobs = []

    for i in range(5):
        p = ProcessTest()
        jobs.append(p)
        p.start()
        p.join()