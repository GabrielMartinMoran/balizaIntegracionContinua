import _thread
import time
 
def print_thread(number):
  while True:
    print("Hello from thread",number,"\n")
    time.sleep(2)

def startThreads():
	_thread.start_new_thread(print_thread, ([1]))
	_thread.start_new_thread(print_thread, ([2]))
	print("THREADS INICIADOS")

startThreads()
