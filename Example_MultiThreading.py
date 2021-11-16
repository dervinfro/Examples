#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:26:15 2021

@author: user
"""

import threading

from pprint import pprint

import time
#%%

def new_func():
	pprint(threading.activeCount())
	print()
	pprint(threading.enumerate())
	print()
	pprint(threading.current_thread())
	
# Output: 6
# Results below
new_func()
'''
[<_MainThread(MainThread, started 4616117760)>,
 <Thread(Thread-2, started daemon 123145357893632)>,
 <Heartbeat(Thread-3, started daemon 123145363148800)>,
 <HistorySavingThread(IPythonHistorySavingThread, started 123145369477120)>,
 <Thread(Thread-4, started 123145375805440)>,
 <ParentPollerUnix(Thread-1, started daemon 123145381060608)>]

<_MainThread(MainThread, started 4616117760)> - REF line 18 (current_thread)
'''

def func():
	print('Hello new func.')

# Create and run 1st Thread in Python
# Pass along arugment to the constructor of the Thread class
x = threading.Thread(target = func)

x.start()

#%% Naming and Joining Threads


def sleep_func():
	time.sleep(2)
	print('Hello sleep func')
	
x = threading.Thread(target = sleep_func,
					 name = 'brand_new_thread')

# Output: 7
# Results below:
x.start()

x.join()

print('Main Thread')

pprint(threading.activeCount())
print('**')
pprint(threading.enumerate())
print('**')
pprint(threading.currentThread())
'''
7
**
[<_MainThread(MainThread, started 4616117760)>,
 <Thread(Thread-2, started daemon 123145357893632)>,
 <Heartbeat(Thread-3, started daemon 123145363148800)>,
 <HistorySavingThread(IPythonHistorySavingThread, started 123145369477120)>,
 <Thread(Thread-4, started 123145375805440)>,
 <ParentPollerUnix(Thread-1, started daemon 123145381060608)>,
 <Thread(brand_new_thread, started 123145386315776)>] # see: brand_new_thread
**
<_MainThread(MainThread, started 4616117760)>
Hello sleep func
'''

#%% Deriving the Thread Class

# Output(Child Thread): Thello from my func. My name is:  Thread-150
def func():
	time.sleep(2)
	print('Thello from my func. My name is: ', threading.current_thread().getName())
	
x = threading.Thread(target = func)

x.start()
x.join()

# Output (Main Thread): This is the main thread.  My name is:  MainThread
print('This is the main thread.  My name is: ', threading.current_thread().getName())

def calc_square(n):
	result = n * n
	print('the number {} squares to {}'.format(n, result))
	
square_list = []
num_list = [1,2,3,4]

for n in num_list:
	
 	# terminating comma only required in case of functions with single arg
# 	 The comma is given for python to understand it is a tuple
	thread = threading.Thread(target = calc_square,
						   args=(n, ))
	square_list.append(thread)
	
	thread.start()
	thread.join()
	
	
# a class which sub-classes the Thread Class
# When extending the Thread class, a Child class can only override two methods:
# 	init() method
# 	run() method
# No other method can be overridden.


# Output: Helllo from func. My name is Thread-164
# Output: Control returned to MainThread
class DerivedThread(threading.Thread):
	
	def run(self):
		time.sleep(2)
		print('Helllo from func. My name is {}'.format(threading.current_thread().getName()))
		
obj = DerivedThread()

obj.start()
obj.join()

print('Control returned to {}'.format(threading.current_thread().getName()))

# Creating Threads w/o extending Thread Class

class RegularClass:
	
	def print_list(self):
		mixed_list = [7,6,11,'hello',5.1,'rose']
		
		for x in mixed_list:
			print('Printing from the Child Thread: ', x)
			time.sleep(1)
			
obj1 = RegularClass()

x = threading.Thread(target = obj1.print_list)

x.start()
x.join()

print('Control returned to: {}'.format(threading.current_thread().getName()))

#%% Running Threads Concurrently

'''
Advantages of multithreading ( mainly It inceases the performance by reducing 
  the response time 
1) Enhanched performance time by decreasing the development time
2) Simplified and streamlined program coding
3) Simultaneous and prallel occurance of tasks
4) Better use of CPU resource
'''

def greetings1():
	for i in range(6):
		print('hello')
		time.sleep(1)
		
def greetings2():
	for i in range(6):
		print('world')
		time.sleep(1)
		
starttime = time.time()

greetings1()
greetings2()

endtime = time.time()

# Output: Total time:  12.03472900390625
print('Total time: ', endtime - starttime)

# Same as above, only add in threading.

def greetings_1():
	for i in range(6):
		print('hello')
		time.sleep(1)
		
def greetings_2():
	for i in range(6):
		print('world')
		time.sleep(1)
		
starttime = time.time()

t1 = threading.Thread(target = greetings_1)
t2 = threading.Thread(target = greetings_2)

t1.start()
t2.start()

t1.join()
t2.join()

endtime = time.time()

# Output: Total time:  6.025590896606445
print('Total time: ', endtime - starttime)

#%% Race Conditions

'''
Thread Synchronisation ensures that two or more concurrent threads running 
	simultaneously do not execute the segment (critical section ) of the code 
	where the shrared memory is accessed.
There are synchronization primitives for synchronising threads in threading module
- Locks
- Rlocks
- Semaphores
- Events
- Conditions
'''

amount = 0 

def deposit(dep_amount):
	
	global amount
	
	for i in range(dep_amount):
		amount += 1
		
def two_deposit_threads(dep_amount):
	
	t1 = threading.Thread(target = deposit, args=(dep_amount, ))
	t2 = threading.Thread(target = deposit, args=(dep_amount, ))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
two_deposit_threads(100000)

'''
If this is run for multiple iterations, the Balance Amount will change.
This is because there are two threads and both of them are accessing the same
data.  This is known as a race condition.
'''
print('Balance amount = {}'.format(amount))

#%% Thread Sync with Locks

'''
**LOCKS**
Race condition can be solved using Lock
Using Lock class objectTo block the threads to access the shared data at the same time.
It has two methods acquire and release . acquire method locks the shared data 
for another thread to access it, only after unlocking by the release method, 
shared data can be accessed
'''

def deposit(dep_amount, dep_lock):
	
	global amount
	
	for i in range(dep_amount):
		dep_lock.acquire()	# This line and...
		amount += 1
		dep_lock.release() # This line are responsible for locking the variable
		
def two_deposit_threads(dep_amount):
	lock = threading.Lock()
	
	t1 = threading.Thread(target = deposit, args = (dep_amount, lock))
	t2 = threading.Thread(target = deposit, args = (dep_amount, lock))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
amount = 0

two_deposit_threads(10000)

print('Balance amount = {}'.format(amount))

#  If release() is called in the unlock state, a RunTimeError() is raised
# NOTE: Remove line 275 and re-run code to see RunTimeError

'''
**RLock (re-entrant lock)**
The standard Lock does not know which thread is currently holding the lock. 
If the lock is held, any thread that attempts to acquire it will block, 
even if the same thread itself is already holding the lock. 
In such cases, RLock is used
The main difference between Lock and RLock is that when you try to acquire 
the lock which is already acquired by the same thread it doesn't block the 
thread unlike the Lock().
'''
lock = threading.Lock()

# Use timeout function to avoid infinite acquire loop
print('first try: ', lock.acquire())
print('second try: ', lock.acquire(timeout=2))


lock = threading.RLock()

print('first try: ', lock.acquire())
print('second try: ', lock.acquire())
print('Third try ',lock.acquire())

#%% Simulation a Deadlock

'''
Conditions for a deadlock:
Mutual Exclusion: One or more than one resource are non-sharable 
(Only one process can use at a time)
Hold and Wait: A process is holding at least one resource and waiting for resources.
No Preemption: A resource cannot be taken from a process unless the process 
releases the resource.
Circular Wait: A set of processes are waiting for each other in circular form.
'''

dataone = 3
datatwo = 5

def my_process(lockone, locktwo):
	
	global dataone
	global datatwo
	
	lockone.acquire()
	print(threading.currentThread().name, 'Incrementing data one')
	dataone += 1
	time.sleep(1)
	
	locktwo.acquire()
	print(threading.currentThread().name, 'Incrementing data two')
	datatwo += 1
	time.sleep(1)
	
	lockone.release()
	locktwo.release()
	
lock1 = threading.Lock()
lock2 = threading.Lock()

t1 = threading.Thread(target = my_process, args = (lock1, lock2))
t2 = threading.Thread(target = my_process, args = (lock1, lock2))

t1.start()
t2.start()

t1.join()
t2.join()

# %% Avoiding a Deadlock

#%% Semaphores - Part 1

'''
Semaphores
This is one of the oldest synchronization primitives in the history of computer 
science, invented by the early Dutch computer scientist Edsger W. Dijkstra
Semaphores are typically used for limiting a resource
Semaphores are simply advanced counters
An acquire() call to a semaphore will block only after a number of threads 
have acquire()ed it.
The associated counter decreases per acquire() call, and increases per 
release() call.

Initialize a semaphore
The default internal variable = 1. This represents the maximum number of 
threads which can acquire the semaphore at any time
'''
semaphore = threading.Semaphore()

def my_func():
	
	semaphore.acquire()
	
	time.sleep(1)
	print(threading.currentThread().name,'acquired the semaphore')
	print('Semaphore value after acquire: ', semaphore._value)
	
	time.sleep(5)
	
	semaphore.release()
	
	print('Semaphore value after release: ', semaphore._value)
	
t1 = threading.Thread(target = my_func)
t2 = threading.Thread(target = my_func)

# Output: Initial semaphore value:  1
print('Initial semaphore value: ', semaphore._value)

starttime = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

endtime = time.time()

print('Total time: ', endtime - starttime)

semaphore = threading.Semaphore(value=3)

t1 = threading.Thread(target = my_func)
t2 = threading.Thread(target = my_func)
t3 = threading.Thread(target = my_func)
t4 = threading.Thread(target = my_func)
t5 = threading.Thread(target = my_func)
t6 = threading.Thread(target = my_func)

starttime = time.time()

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

endtime = time.time()

print('Total time: ', endtime - starttime)

#%% Semaphore 2
'''
While creating a semaphore object threading.Semaphore() input internal variable 
can not be less than zero

Using a Semaphore to synchronize threads
We can use the following programe as a ordering software in a resturant, 
where the ordering and serving is automoted

The internal variable is set to 0
By the resturant() function the lock been released which increased the variable 
to 1 so that customer() function semaphore.acquire() can be invoked
'''

semaphore = threading.Semaphore(0)

order_num = 0 

def place_order():
	print('order placed')
	semaphore.acquire()
	print('custermer order number is: ', order_num)
	
def prepare_order():
	
	global order_num
	time.sleep(3)
	order_num += 1
	
	print('Prepareing order number: ', order_num)
	semaphore.release()
	
for i in range(0,6):
	t1 = threading.Thread(target=place_order)
	t2 = threading.Thread(target=prepare_order)

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
print('program terminated')

# A Semaphore provides a non-bounded counter which allows you to call release() any number of times for incrementing

semaphore = threading.Semaphore()

# Output: 1
semaphore._value

semaphore.acquire()

# Output: 0
semaphore._value

semaphore.release()

# Output: 1
semaphore._value

semaphore.release()

# Output: 2
semaphore._value

semaphore.release()
semaphore.release()
semaphore.release()

# Output: 5
semaphore._value

# BoundedSemaphore provides a bounded counter, which raises an error if a 
# release() call tries to increase the counter beyond its maximum size
semaphore = threading.BoundedSemaphore(1)

# Output: 1
semaphore._value

semaphore.acquire()

# Output: 0
semaphore._value

semaphore.release()

# Output: 1
semaphore._value

# ValueError: Semaphore released too many times
semaphore.release()

#%% The Event Object

'''
Events
This is one of the simplest mechanisms for communication between threads: 
	one thread signals an event and other threads wait for it.
An event object manages an internal flag that can be set to true with the 
	set() method and reset to false with the clear() method.
The wait() method blocks until the flag is true.
'''

event = threading.Event()

dir(event)

event.set()
print(event.is_set())

event.wait()
print(event.is_set())

event.clear()
print(event.is_set())

# event.set()
# print(event.is_set())

# event.clear()
# print(event.is_set())

# event.wait()
# print(event.is_set())


meeting = threading.Event()

def hold_meeting():
	
	meeting.set()
	print('event is set. the meeting has begun')
	
	time.sleep(6)
	
	print('the meeting is complete. clearing the event')
	meeting.clear()
	

def enter_conf_room():
	
	time.sleep(1)
	meeting.wait()
	 
	while meeting.is_set():
		
		print('waiting for the meeting to end')
		time.sleep(0.5)
		
	print('the meeting is done. enter the conf room')
	
t1 = threading.Thread(target = hold_meeting)
t2 = threading.Thread(target = enter_conf_room)

t1.start()
t2.start()

t1.join()
t2.join()

#%% The Condition Object

'''
Conditions
A Condition object is simply a more advanced version of the Event object.

It too acts as a communicator between threads and can be used to notify() 
other threads about a change in the state of the program
'''

import random

condition = threading.Condition()

container = []

counter = 1

moretocome = True

def produce():
	
	global container
	global counter
	global moretocome
	
	for i in range(5):
		
		time.sleep(random.randrange(2,5))
		condition.acquire()
		
		item = "News items #" + str(counter)
		
		container.append(item)
		counter += 1
		
		print('Produced: ', item)
		condition.notify_all()
		
		condition.release()
		
	moretocome = False
	
def consume():
	
	global moretocome

	while(moretocome):
		
		condition.acquire()
		condition.wait()
		
		time.sleep(random.random())
		print(threading.currentThread().getName(), ' acquired: ', container[-1])
		
		condition.release()
		
producerthread = threading.Thread(target=produce)

c_one_thread = threading.Thread(target = consume, name = 'New Site One')

c_two_thread = threading.Thread(target = consume, name = 'News Site Two')

c_three_thread = threading.Thread(target = consume, name = 'News Site Three')

threads = [producerthread,
		   c_one_thread,
		   c_two_thread,
		   c_three_thread,
	]

for t in threads:
	t.start()
	
for t in threads:
	t.join()
	
time.sleep(1)

print('all done')


































