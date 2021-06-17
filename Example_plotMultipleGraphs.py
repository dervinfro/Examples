import matplotlib.pyplot as plt
import numpy as np

'''
NOTE: As of 6JAN2021, see the Example - Logistic Regression -2.py
- this example shows subplots using sns.heatmap
'''

fig = plt.figure(figsize=(8,8))
'''
fig.add_subplots(num1, num2, num3)
	num1 = number of graphs on page
	num2 = number of graphs per line, ie if num2 = 3, then the graph will take up a third of the space for 		that particular line. 
			if this is 1, then it refs to num3 to where it will print on the page
			if this is not 1, then it shows how the graph gets sized on the first line
	num3 = location of graph on page (this value can never be larger than num1)
'''

ax1 = fig.add_subplot(4,2,3) # 4 graphs, 2 graphs per line, position 3 (out of 4 positions)
ax2 = fig.add_subplot(4,2,4) 
ax3 = fig.add_subplot(4,1,4)

ax1.plot(np.random.randn(50).cumsum(), 'k--')
ax1.set_title("ax1 value")

ax2.hist(np.random.randn(50).cumsum(), bins=10, color='g')
ax2.set_title("ax2 value")

ax3.plot(np.random.randn(100, 3).cumsum(0))
ax3.legend(('line1','line2','line3'),loc='upper right')
ax3.set_title("ax3 value")

plt.show()
