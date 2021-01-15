import time

while True:
    perf=int(time.perf_counter())
    if(perf>10):
        perf=0
    print(perf)