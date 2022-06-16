import multiprocessing
import time
def process_gol():
    nume = multiprocessing.current_process().name
    print("\nPornesc un proces numit : {}".format(nume))
    time.sleep(5)
    print("Am terminat procesul numit : {}".format(nume))

if __name__ == "__main__":
    proces_demon = multiprocessing.Process(name="proces_demon",target=process_gol)
    proces_demon.daemon = True

    proces_normal = multiprocessing.Process(name="proces_normal",target=process_gol)
    proces_normal.daemon = False

    proces_normal.start()
    proces_demon.start()
    time.sleep(5)