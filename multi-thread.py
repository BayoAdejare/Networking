#!/usr/bin/python
import os
from threading import Thread
import time
start=time.ctime()
print(start)

scan="ping -c1 -w1 "
max=65

class threadclass(Thread):
    def __init__ (self,ip):
        Thread.__init__(self)
        self.ip = ip
        self.status = -1
    def run(self):
        result = os.popen(scan+self.ip,"r")
        self.status=result.read()

threadlist = []

for host in range(1,max):
    ip = "10.0.0."+str(host)
    current = threadclass(ip)
    threadlist.append(current)
    current.start()

for t in threadlist:
    t.join()
    print("Status from ",t.ip,"is",repr(t.status))

print(start)
print(time.ctime())