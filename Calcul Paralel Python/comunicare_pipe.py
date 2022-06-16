import multiprocessing
def creare_elemente(pipe):
    pipe_iesire,_ = pipe
    for element in range(4):
        pipe_iesire.send(element)
    pipe_iesire.close()

def multiply_elements(pipe1,pipe2):
    close,pipe_intrare = pipe1
    close.close()
    pipe_iesire,_ = pipe2
    try:
        while True:
            element = pipe_intrare.recv()
            print("Am primit in pipe1: {}".format(element))
            x = element * element
            pipe_iesire.send(x)
            print("Am trimis in pipe2: {}".format(x))
    except EOFError:
        pipe_iesire.close()

if __name__ == "__main__":
    pipe1 = multiprocessing.Pipe(True)
    process_pipe1 = multiprocessing.Process(target=creare_elemente,args=(pipe1,))
    process_pipe1.start()

    pipe2 = multiprocessing.Pipe(True)
    process_pipe2 = multiprocessing.Process(target=multiply_elements,args=(pipe1,pipe2))
    process_pipe2.start()

    pipe1[0].close()
    pipe2[0].close()
    try:
        while True:
            print("Am scos elementul : {}".format(pipe2[1].recv()))
    except EOFError:
        print("End")