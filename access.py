from array import *
arr1=array('i',[1,2,3,4,5,6])

def access(array,index):
    if index >= len(arr1):
        print("No element found")
    else:
        print(array[index])
access(arr1,-1)