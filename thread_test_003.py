#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
    * thread.allocate_lock() : critical section에 사용할 lock 객체 리턴
    * lock.acquire() : lock을 건다
    * lock.release() : 걸었던 lock 해제
    * lock.locked() : lock이 걸려있는지 검사. 락이 걸려 있으면 True, 아니면 False
'''
import thread, time

g_count = 0
# lock 객체 생성
lock = thread.allocate_lock()

def counter(id, count):
     global g_count
     for i in range(count):
         print 'id %s --> %s' % (id, i)
         # lock 건다
         lock.acquire()
         # 전역변수 핸들링
         g_count = g_count + 1
         # lock 해제
         lock.release()

for i in range(5):
     thread.start_new_thread(counter, (i, 5))

time.sleep(1)
print 'Total Count = ', g_count
print 'Exiting'