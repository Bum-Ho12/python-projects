import threading
import time

start_time = time.perf_counter()

def called_thread():
    print("Sleeping 1 second")
    time.sleep(1)
    print("finished sleeping...")

first_thread = threading.Thread(target=called_thread)
second_thread = threading.Thread(target=called_thread)
third_thread = threading.Thread(target=called_thread)

first_thread.start()
second_thread.start()
third_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()

finish_time = time.perf_counter()
print(f"finished in {round(finish_time-start_time,2)} second(s)")
