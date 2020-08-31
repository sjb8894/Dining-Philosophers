import threading
import time
import sys
global philosophers_num
global self
go = True

class Philosopher(threading.Thread):
    def __init__(self, threadID, leftLock, rightLock):
        threading.Thread.__init__(self)
        self.id = threadID
        self.leftLock = leftLock #left and right lock come from list of forks that are lock objects
        self.rightLock = rightLock


    def run(self):
        global go
        while go:

            print(f"philosopher {self.id} is thinking...")
            while True:
                self.leftLock.acquire(True)
                print(f"philosopher {self.id} picks up left fork.")
                acquired = self.rightLock.acquire(False)
                if acquired:
                    print(f"philosopher {self.id} picks up right fork")
                    break
                else:
                    self.leftLock.release()
                    print(f"philosopher {self.id} puts down left fork.")

            print(f"philosopher {self.id} is eating...")
            self.leftLock.release()
            print(f"philosopher {self.id} puts down left fork.")
            self.rightLock.release()
            print(f"philosopher {self.id} puts down right fork.")

#main method
def main():
    global philosophers_num
    global go
    global self
    philosophers_num = int(sys.argv[1])
    threads = []
    locks = [threading.Lock() for _ in range(philosophers_num)] #creates list of lock obj

    for i in range(philosophers_num):
        thread = Philosopher(i, locks[i], locks[(i+1) % philosophers_num])
        threads.append(thread)

    for i in range(philosophers_num):
        threads[i].start()

    time.sleep(2)
    go = False

main()
