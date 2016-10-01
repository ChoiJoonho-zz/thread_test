#!/usr/bin/python
#-*- coding: utf-8 -*-
#  thread 종료 대기
import thread, time

# 생성할 Thread 갯수 지정
NumberOfThread = 5
# 실행중인 Thread 갯수
ThreadsLeft = NumberOfThread

# Critical Section에 사용할 lock 객체 생성
lock = thread.allocate_lock()

# Thread 종료처리 함수
def threadexit(id):
     global ThreadsLeft
     print 'thread %d is quitting' % id
     lock.acquire()
     ThreadsLeft -= 1
     lock.release()

def counter(id, count):
     for i in range(count):
         print 'id %s --> %s' % (id, i)
     threadexit(id) # thread 종료처리 함수 호출

# NumberOfThread 만큼 Thread 생성
for i in range(NumberOfThread):
     thread.start_new_thread(counter, (i, 5))

# 모든 Thread가 종료될 때 까지 대기
while ThreadsLeft:
     time.sleep(0.1)

print 'Exiting'