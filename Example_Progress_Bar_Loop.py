from tqdm import tqdm
from time import sleep
import timeit

max_iter = 10
iter = 0

def prog_bar(iter):
	for iter in tqdm(range(iter, max_iter)):
		sleep(0.2)
	return iter
	
prog_bar(iter)
print(timeit.default_timer())	
