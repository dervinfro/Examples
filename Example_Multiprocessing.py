#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 21:51:27 2021

@author: user
"""

#%% Intro Python Queues

'''
The Queues are a great mechanism when we need to exchange information between 
	threads
There are three (3) types queues:
FIFO queue
LIFO queue
Priority queue
'''

import queue
import time

q = queue.Queue()

# Output: deque([])
q.queue


for i in range(7):
	q.put(i)
	
# Output: deque([0, 1, 2, 3, 4, 5, 6])
q.queue

# Output: False
q.empty()

'''
Output:
0
1
2
3
4
5
6
'''
while not q.empty():
	print(q.get())
	
# Output: deque([])
q.queue

# Output: True
q.empty()

'''
LIFO Queue
In contrast to the standard FIFO implementation of Queue, the LifoQueue uses 
last-in, first-out ordering (normally associated with a stack data structure).
'''
q = queue.LifoQueue()

for i in range(7):
	q.put(i)
'''
Output:
6
5
4
3
2
1
0
'''
while not q.empty():
	print(q.get())
	
'''
Priority Queue
PriorityQueue uses the sort order of the contents of the queue to decide which 
	to retrieve.
'''
	
q = queue.PriorityQueue()

q.put(5)
q.put(4)
q.put(1)
q.put(3)
q.put(2)
	
'''
Output:
1
2
3
4
5
'''
while not q.empty():
	print(q.get())
	
	
	
#%% Multithreading w Python Queues

q = queue.Queue()

q.put(6)
q.get()
q.empty()

'''
output`: The shell doesn't return anything as the thread signal is blocked Go 
to the kernel and click on `intrrupt`
'''
# q.get()

import threading
import random
counter = 1
moretocome = True

class Producer(threading.Thread):
	
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue = queue
		
	def run(self):
		
		global counter
		global moretocome
		
		for i in range(5):
			
			time.sleep(random.randrange(2,5))
			item = "news item # " + str(counter)
			
			self.queue.put(item)
			counter += 1
			
			print('produced: ', item)
			
		moretocome = False
		
class Consumer(threading.Thread):
	
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue = queue
		
	def run(self):
		
		while (moretocome):
			item = self.queue.get(timeout=10)
			time.sleep(random.random())
			print(threading.current_thread().getName(), 'popped: ', item)
			
		print(threading.currentThread().getName(),'Exiting....')
		
		
q = queue.Queue()

producerthread = Producer(q)
consumerthread = Consumer(q)

producerthread.start()
consumerthread.start()

producerthread.join()
consumerthread.join()



#%% Creating Processes

'''
Multiprocessing is a process which allow spawning i.e it creates child process 
	and execute them, in multithreading child threads are created and executed, 
	here instead of child threads child processes or sub processes are created
The main advantage of multiprocessing is that global interpreter has no effect 
	on it, due to this, the multiprocessing module allows the programmer to fully 
	leverage multiple processors on a given machine.
'''


from multiprocessing import Process, current_process

def square(number):
	
	time.sleep(1)
	result = number * number
	
	processid = current_process().pid
	processname = current_process().name
	
	print('Process ID {} and name {}'.format(processid, processname))
	
	print('The number {} squares to {} \n'.format(number, result))
	

numbers = [1,2,3,4]

starttime = time.time()

for i, number in enumerate(numbers):
	
	process = Process(target = square, args=(number,))
	process.start()
	
process.join()
	
endtime = time.time()

print(endtime - starttime)
	
	
#%% Comparing Multiprocessin and Multithreading

import multiprocessing
import threading

square_result = []


'''
In Ref to the Square Result @ line 258
Note: Every process has its own address space(virtual memory). Thus program 
variables are not shared between two processes. We need to use interprocess 
communication (IPC) techniques if we want to share data between two processes 
which will be shown further
'''

def squares(numbers):
 	
 	global square_result
 	
 	for n in numbers:
         print('square of {} is {}\n'.format(n, n*n))
         square_result.append(n*n)

# 		
# def cube(numbers):
#  	for n in numbers:
#          print('cube of {} is {}'.format(n, n*n))
		
numlist = [1,2]

# NOTE: When p1 is threading, data is more easily shared (see: squares_result)
p1 = threading.Thread(target=squares, args=(numlist,))
# p1 = multiprocessing.Process(target=squares, args=(numlist,))
# p2 = multiprocessing.Process(target=cube, args=(numlist,))

p1.start()
# p2.start()

p1.join()
# p2.join()

print(square_result)

print('\nCompleted')

#%% Multiprocessing using shared memory


result = []

def squares(numlist):
    
    global result
    for num in numlist:
        result.append(num*num)
       
    print('Child process result: ', result)
        
'''
output`:The child process makes a copy of the globaly declared list and append 
squares inside it that is why the updated list is only accessible inside the 
child process
'''

numlist = [1,2,3,4]

p1 = multiprocessing.Process(target=squares, args=(numlist,))

p1.start()
p1.join()

# output`: But main process is printing the initial empty list
print('main process result variable: ', result)

# Method 1 - Sharing Data Using Shared Memory

'''
The main agenda behind the following operation:

    We are creating some variable in the main process, and changing them in the 
    child process, after that we want to see that whether we can see the change 
    in the variables if we call them from the main process
'''
def square_list(numlist, result, square_sum):

    for idx, num in enumerate(numlist):
        result[idx] = num * num
        
    square_sum.value = sum(result)
    
# 4 = length of Array
result = multiprocessing.Array('i', 4)
square_sum = multiprocessing.Value('i')

p = multiprocessing.Process(target = square_list,
                            args = (numlist, result, square_sum))

p.start()
p.join()

list(result)

square_sum.value

#%% Multiprocessing using Manager Class

'''
Whenever a python program starts, a server process is also started. 
From there on, whenever a new process is needed, the parent process connects 
to the server and requests it to fork a new process. 
We can save the data in this server process which later can be shared among 
different child processes.

multiprocessing module provides a Manager class which controls a server process. 
Hence, this class provide way to share data using server process
'''
def getdata(datalist):
    for data in datalist:
        print('Name: {} Score: {}'.format(data[0],data[1]))
        
def appenddata(newdata, datalist):
    datalist.append(newdata)
    print('New data appended')
    
database = ([('rowan',2),('bodhi',8),('nala',12)])

newdata = (['dad',45])

p1 = multiprocessing.Process(target = appenddata,
                           args = (newdata, database))
p2 = multiprocessing.Process(target = getdata,
                             args = (database,))

'''
output: After execution of p2 process, the new data elements should be visible 
in the data list but it is not visible because while process start to work with 
variables they create their own copy of variable so the p1 process new_data 
is not the one which is printed by the p2 process. Without data sharing the 
processes can not coordinate with each other
'''

p1.start()
p1.join()

p2.start()
p2.join()

# Main process
database


with multiprocessing.Manager() as manager:
    
    database = (manager.list([('rowan',2),('bodhi',8),('nala',12)]))
    newdata = ('dad',45)
    
    p1 = multiprocessing.Process(target = appenddata,
                                 args = (newdata, database))
    p2 = multiprocessing.Process(target = getdata,
                                 args = (database,))
    
    p1.start()
    p1.join()
    
    p2.start()
    p2.join()
    
    print('Data available to the manager: ',database)
    
    '''
    `output`: Process p2 asks server process for the updated list that is 
    saved in the variable `data`, hence we can see the `new data` in it 
    '''
    
#%% Sync Concurrent Processes with Locks

'''
The concept of multiprocessing lock is similar to the lock in multi threading, 
without the use of lock when a shared data is accessed by a single process then 
other process can also access the shared data which will result a corrupt output
'''

def deposit_wo_mp(balance, amount):
    for i in range(100):
        time.sleep(0.1)
        balance += amount
        
    return balance

def withdrawl_wo_m(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance -= amount
        
    return balance

balance = 600
balance

# ctypes
balance = deposit_wo_mp(balance, 5)

balance = withdrawl_wo_m(balance, 5)

print('final balance: ', balance)



def deposit_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value += amount

def withdraw_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value -= amount
        
balance = multiprocessing.Value('i',600)

d = multiprocessing.Process(target = deposit_without_lock,
                            args = (balance, 5))

w = multiprocessing.Process(target = withdraw_without_lock,
                            args = (balance, 5))

d.start()
w.start()

d.join()
w.join()

print('final balance: ', balance.value)

'''
`output`: When running for the first time the output may be correct but if we 
run it again and again then all we get is corrupt output, to solve this 
problem we use `Lock`
'''

def deposit_with_lock(balance, amount, lock):
    
    for i in range(100):
        time.sleep(0.01)
        
        lock.acquire() 
        
        balance.value += amount
        
        lock.release()
        
    
def withdraw_with_lock(balance, amount, lock):
    
    for i in range(100):
        time.sleep(0.01)
        
        lock.acquire()
        
        balance.value -= amount
        
        lock.release()
        
balance = multiprocessing.Value('i',600)
lock = multiprocessing.Lock()

d = multiprocessing.Process(target = deposit_with_lock,
                            args = (balance, 5, lock))

w = multiprocessing.Process(target = withdraw_with_lock,
                            args = (balance, 5, lock))

d.start()
w.start()

d.join()
w.join()

print('final balance: ', balance.value)

#%% Communication Between Processes

'''
Effective use of multiple processes usually requires some communication between 
them, so that work can be divided and results can be aggregated.

multiprocessing supports two types of communication channel between processes:

Queue
Pipe
'''

# Method 1: Queue
'''
a simple way to communicate between processes and pass messages back and forth. 
Any python object can be exchnaged through a queue
'''
def is_even(numbers, q):
    for n in numbers:
        if n % 2 == 0:
            q.put(n) 
        
def print_numbers(q):
    while not q.empty():
        print(q.get())
        
q = multiprocessing.Queue()

p1 = multiprocessing.Process(target = is_even,
                             args = (range(10), q))

p2 = multiprocessing.Process(target = print_numbers,
                             args = (q, ))

p1.start()
p2.start()

p1.join()
p2.join()

# Method 2: Pipe
'''
The Pipe( ) function returns a pair of connection objects connected by a pipe 
which by default is duplex (two-way)
'''

def sender(connection, greets):
    for greet in greets:
        connection.send(greet) 
    connection.close()       
    
def recipient(connection):
    while True:
        greet = connection.recv() 
        if greet == "STOP": 
            break
        print(greet)
        
msgs = ["Hello", "Hola", "Guten Tag", "STOP"]

sending_pipe, receiving_pipe = multiprocessing.Pipe()

multiprocessing.Pipe()

p1 = multiprocessing.Process(target=sender, 
                             args=(sending_pipe, msgs))
p2 = multiprocessing.Process(target=recipient, 
                             args=(receiving_pipe,))

p1.start()
p2.start()

p1.join()
p2.join()
















































