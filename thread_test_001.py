#!/usr/bin/python
#-*- coding: utf-8 -*-

import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   try:
      count = 0
      while count < 5:
         time.sleep(delay)
         count += 1
         print "%s: %s" % ( threadName, time.ctime(time.time()) )
   except:
         print "Error: unable to start thread"

# Create two threads as follows

thread.start_new_thread(print_time, ("Thread-1", 0.1, ) )
# thread.start_new_thread( print_time, ("Thread-2", 0.1, ) )

# time.sleep(5)
