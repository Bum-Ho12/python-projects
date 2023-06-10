from multiprocessing import Process, Pipe
from time import sleep

def worker(conn):
    print('Worker - started now sleeping for 1 second')
    sleep(1)
    print('Worker - sending data via Pipe')
    conn.send(' Message -> _______ Hello, World _______')
    print('Worker - closing worker end of connection\n')
    conn.close()


def main():
    print('Main - Starting, creating the Pipe')
    print('Main - Setting up the process')
    main_connection, worker_connection = Pipe()
    p = Process(target = worker, args=[worker_connection])
    print('Main - Starting the process')
    p.start()
    print('Main - Wait for a response from the child process')
    print(main_connection.recv())
    print('Main - closing parent process end of connection')
    main_connection.close()
    print('Main - Done')

if __name__ == '__main__':
    main()
