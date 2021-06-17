# -*- coding: utf-8 -*-
"""
Spyder Editor

https://support.minitab.com/en-us/minitab-express/1/help-and-how-to/modeling-statistics/regression/how-to/correlation/interpret-the-results/#step-3-examine-the-monotonic-relationship-between-variables-spearman

https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
"""

from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr

import seaborn as sns
from numpy import cov


# seed random number generator
seed(1)

# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

# summarize data with mean and standard deviation
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
print('')

# Longhand covariance math equation
cov_x_y = (sum ((data1 - mean(data1)) * (data2 - mean(data2))) ) * (1/(len(data1) - 1))

# Alternate plot method using Seaborn
# points are blue
# OLS regression line is red
sns.regplot(x=data1, y=data2, scatter_kws={'color':'blue'}, line_kws={'color':'red'})

covariance = cov(data1, data2)
print('Covariance Matrix:', covariance, sep='\n')
print('')

# Pearson Correlation Coef (Longhand Math)
# See corr imported function below for comparison
print('Pearson Correlation Coef. (Longhand Math):', covariance / (std(data1) * std(data2)), sep='\n')
print('')

corr, _ = pearsonr(data1, data2)
print('Pearson Correlation Coef. (Import):', corr)