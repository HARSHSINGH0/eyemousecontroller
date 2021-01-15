import time

while True:

    perf=int(time.perf_counter())
    if(perf>5):
        perf=0
        print(perf)
        perf=int(time.perf_counter())
    print(perf)