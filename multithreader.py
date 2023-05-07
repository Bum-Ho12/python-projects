import threading

class Workers():
    def startWorker(worker):
        threading.Thread(target = worker).start()

if __name__ =='__main__':
    Workers.startWorker()

