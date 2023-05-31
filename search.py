from array import *
arr1=array('i',[1,2,3,4,5,6])

def search(array,value):
    for i in array:
        if i==value:
            return array.index(value)
    return 'Element is not in the array'
print(search(arr1,4))