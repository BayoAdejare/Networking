#!/usr/bin/python
import os
import sys

scan = "ping -c1 -w1 "
max = 62

for h in range(1, max):
    ip = "10.0.0." + str(h)
    out = os.popen(scan + ip, "r")
    sys.stdout.flush()
    print(out.read())
