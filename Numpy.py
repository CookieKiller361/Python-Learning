#just some beginner NumPy code 
import numpy as np

arraynp = np.array([1,2,3,4,5,6])


#or
ListTest=[1,2,3,4,5,6]
arrayTestList = np.array(ListTest)

print(arraynp)
print(f'\n{arrayTestList}')

#0-Demension Array 
zeroDemensionArray=np.array(34)
#1-Demension Array
oneDemensionArray=np.array([1,2,3])
#2-Demension Array
twoDemensionArray=np.array([[1,2,3],[1,2,3]])
#3-Demension Array
threeDemensionArray=np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])