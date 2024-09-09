from array import *
def selection_sort(data_array):
    for i in range(len(data_array)):
        minimum=i
        for j in range(i+1,len(data_array),1):
            if data_array[j]<data_array[minimum]:
                minimum=j
        data_array[i],data_array[minimum]=data_array[minimum],data_array[i]

data=array('i',[])
size=int(input("Input size of the array"))
print("Input elements into the array")
for u in range(size):
    inputs=int(input())
    data.append(inputs)
print("Unsorted array elements")
for o in data:
    print(o,end=" ")
selection_sort(data)
print("Sorted array elements")
for r in data:
    print(r,end=" ")



