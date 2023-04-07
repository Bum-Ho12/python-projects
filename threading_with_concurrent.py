import time
import concurrent.futures as fc

start_time = time.perf_counter()

def called_thread():
    print("Sleeping 1 second...")
    time.sleep(1)
    return 'Done Sleeping...'

with fc.ThreadPoolExecutor() as threader:
    results = [threader.submit(called_thread) for _ in range(3)]
    for f in fc.as_completed(results):
        print(f.result())

finish_time = time.perf_counter()

print(f"Finished in {round(finish_time-start_time,2)} second(s)")