import numpy as np
twoDArray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)

#inserting a row at start

new2DArray=np.insert(twoDArray,-1,[[0,0,0]],axis=0)
print(new2DArray)