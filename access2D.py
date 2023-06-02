import numpy as np
twoDArray=np.array([[1,2,3],[4,5,6],[7,8,9]])

def access(array , rowIndex , colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        return 'invalid index'
    else:
        return(array[rowIndex][colIndex])

print(access(twoDArray , 1, 2))