import time

def get_function_exec_time(message, function, *args):
    start_time = time.time()
    print(message + str(function(*args)))
    execTime = (time.time() - start_time) * 1000
    print("Time: %.5s ms" % execTime)
