
import pandas as pd
import numpy as np
from scipy import stats
import pingouin as pg
import statsmodels.formula.api as sm


'''
-The t test tells you how significant the differences between groups are; In other words it lets you know if those differences (measured in means) could have happened by chance.
- The t score is a ratio between the difference between two groups and the difference within the groups. 
- A large t-score tells you that the groups are different.
- A small t-score tells you that the groups are similar.
- typically used for sample sets with a size of 30 or less
- if the sample set is greater than 30, a z-test is used.

- Every t-value has a p-value to go with it. 
- A p-value is the probability that the results from your sample data occurred by chance. 
- P-values are from 0% to 100%. 
- For example, a p value of 5% is 0.05. 
- Low p-values are good; They indicate your data did not occur by chance. 
- EXAMPLE: a p-value of .01 means there is only a 1% probability that the results from an experiment happened by chance. In most cases, a p-value of 0.05 (5%) is accepted to mean the data is valid
SEE: 
https://www.statisticshowto.com/probability-and-statistics/t-test/
https://www.statisticshowto.com/p-value/
https://medium.com/analytics-vidhya/everything-you-should-know-about-p-value-from-scratch-for-data-science-f3c0bfa3c4cc

'''


def t_test():

	x = np.random.randint(0,100,10)
	y = np.random.randint(0,100,10)

	list1 = list(x)
	list2 = list(y)
	print('List 1 & List 2: ', list1, list2, sep='\n')
	print('\n')
	print('Stats T Test (List 1 & List 2): ', stats.ttest_ind(list1, list2), sep='\n')
	print('\n')
	
	#treatment_systolic = [-7.91, -7.98, -7.99, -7.99 , -8.05, -8.03, -8.00, -7.98, -7.96 , -8.00, -8.00, -7.98, -7.94, -7.99, -7.98]
	#control_systolic = [-4.89, -5.07, -5.02, -5.04, -4.95, -5.12, -5.20, -5.21, -5.07, -4.88, -4.96, -5.10]
	#print(stats.ttest_ind(treatment_systolic,control_systolic))
	#Ttest_indResult(statistic=-99.90987090748176, pvalue=4.672960612136045e-34)

	model = pg.ttest(list1, list2)
	print('Pingouin T Test (List 1 & List 2): ', model, sep='\n')
	print('\n\n')
	
	list3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	list4 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
	print('Stats T Test (List 3 & List 4): ', stats.ttest_ind(list3, list4), sep='\n')
	#RESULTS from List3 & List4: Ttest_indResult(statistic=-inf, pvalue=0.0)
	
	list5 = [99, 100, 100, 100, 100, 100, 100, 100, 100, 100]
	list6 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
	print('Stats T Test (List 5 & List 6): ', stats.ttest_ind(list5, list6), sep='\n')

t_test()