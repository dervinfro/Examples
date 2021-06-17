import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



x_list_logit = []
y_list_logit = []
for x in np.arange(0.01, 1, 0.01):
    logit = np.log(x/(1-x))
    x_list_logit.append(round(x,2))
    y_list_logit.append(logit)
    
print(x_list_logit)
print(y_list_logit)
    
x_list_sig = []
y_list_sig = []

for x in np.arange(-10, 10, 1):
    sigmoid = (1/(1 + np.exp(-x)))
    x_list_sig.append(round(x,2))
    y_list_sig.append(sigmoid)
    
print(x_list_sig)
print(y_list_sig)
plt.figure(figsize = (8,8))

#plt.xlabel('X Value')
#plt.ylabel('Logit Value (Y Value)')
#plt.title('Logistic Regression')
#sns.lineplot(x=x_list_logit, y=y_list_logit, color='red', label='Logistic Regression')

plt.xlabel('X Value')
plt.ylabel('Sigmoid Value (Y Value)')
plt.title('Sigmoid Function')
sns.lineplot(x=x_list_sig, y=y_list_sig, color='blue', label='Sigmoid Function')
plt.show()

