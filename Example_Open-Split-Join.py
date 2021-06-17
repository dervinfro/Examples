import numpy as np
from string import punctuation
from collections import Counter


with open('/Users/user/Documents/ROVER LINUX/linux-ROVER-4.19-releaseNotes.txt', 'r') as f:
	data = f.read()
	
data_250 = data.lower() #print up to the first 250 chars and make them all lower case

new_data_250 = ''.join([x for x in data_250 if x not in punctuation])
all_data = new_data_250.split()
#print(all_data, '\n',  '*' * 15, '\n', '*' * 15) #printed as a list
all_data1 = '\n'.join(all_data)
#print(all_data1, '\n',  '*' * 15, '\n', '*' * 15) #after the .join above, all_data1 is a string
words = all_data1.split()
#print(words) #after the .split above, words type is a list
counts = Counter(words)
vocab = sorted(counts, reverse=True)
print("VOCAB: \n", vocab)

print()
vocab_int = {word: ii for ii, word in enumerate(vocab, 1)}
print(vocab_int.keys(), '\n', vocab_int.values())

vocab_np_arr = np.array([1 if ii % 2 == 0 else 0 for ii, word in enumerate(vocab, 1)]) #list comprehension
print(vocab_np_arr)
