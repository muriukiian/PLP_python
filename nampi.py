import numpy as np 
a = np.array([[1, 2], [3, 4], [5,6],[8,7],[9,10]]) 
print(a)

# minimum dimensions 
#import numpy as np 
#a = np.array([1, 2, 3,4,5], ndmin = 0) 
#print(a)

# dtype parameter 
#import numpy as np 
#a = np.array([1, 0, 3], dtype = int) 
#print(a)


a = np.arange(2, 64, 8)
a = a.reshape(4, 2)
print("The original array is: ")
print(a)
print('\n')
print('Modified array is : ')
for x in np.nditer(a):
  print(x)