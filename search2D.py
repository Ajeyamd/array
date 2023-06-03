import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

def search(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'Element exists at the index ' + str(i) + " " + str(j)
    return 'Element does not exists'
print(search(arr,9))