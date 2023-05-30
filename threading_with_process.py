# from multiprocessing import Process
# from time import sleep
# def worker(msg):
#     for i in range(0, 10):
#         print(msg, end='', flush=True)
#         sleep(1)
# print('Starting')
# t2 = Process(target=worker, args='A')
# t3 = Process(target=worker, args='B')
# t4 = Process(target=worker, args='C')
# t2.start()
# t3.start()
# t4.start()

from multiprocessing import Process
from multiprocessing import set_start_method
from time import sleep
import os
def worker(msg):
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
def main():
    print('Starting')
    print('Root application process id:', os.getpid())
    set_start_method('spawn')
    t = Process(target=worker, args='A')
    t.start()
    print('Done')

if __name__ == '__main__':
    main()