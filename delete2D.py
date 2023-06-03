import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

new2DArray=np.delete(arr,0,axis=1)
print(new2DArray)

#If number of rows and columns are equal then time complexcity will be quadratic