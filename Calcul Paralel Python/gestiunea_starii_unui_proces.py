import multiprocessing
import time
import signal

def proces_gol():
    print("Pornesc executia programului")
    time.sleep(0.1)
    print("Opresc executia programului")

if __name__ == "__main__":
    proces_test = multiprocessing.Process(target=proces_gol)
    print("Starea procesului inainte de executie : {}".format(proces_test.is_alive()))
    proces_test.start()
    print("Starea procesului dupa lansarea in executie : {}".format(proces_test.is_alive()))
    proces_test.terminate()
    try:
        print("Procesul s-a terminat : {}".format(proces_gol().is_alive()))
    except AttributeError:
        print("Nu sunt informatii despre comanda terminare")
    proces_test.join()
    try:
        print("Procesul dupa join : {}".format(proces_gol().is_alive()))
    except AttributeError:
        print("Nu exista informatii dupa join")
    if signal.SIG_DFL == proces_test.exitcode:
        print("Procesul dupa un exit code")