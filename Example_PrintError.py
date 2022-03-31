
#########################################
### Nested Try/Except in a While Loop ###
#########################################

import time

while True:
    
    
    try:
        x = int(input('Enter a value to divide by 5:'))
        print(5/x)
        
    except:
        print('this is a general error @ ', time.asctime())
        pass
    # except ZeroDivisionError:
    #     print('this is a zero error @ ', time.asctime())
    #     pass  
    # except TypeError:
    #     print('This is a type error @ ', time.asctime())
    #     pass     
    # except ValueError:
    #     print('This is a value error @ ', time.asctime())
    #     pass
    
    time.sleep(3)
