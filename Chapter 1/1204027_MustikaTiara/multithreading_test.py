from do_something import *
import time
import threading # Agar dapat melakukan multithreading operation dalam python

if __name__ == "__main__":
    start_time = time.time()
    size = 1000000
    threads = 5           
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=do_something(size, out_list))
        jobs.append(thread)
    for j in jobs:
        j.start()

    
    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multithreading time=", end_time - start_time)
	

