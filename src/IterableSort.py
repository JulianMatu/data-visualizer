# IterableSort.py
from sorting_algos import *

class IterableSort:
    def __init__(self, sortingFunc, sequence: list):
        global iterateEvent
        self.sequence = sequence
        self.sortingFunc = sortingFunc
    
    # returns partially sorted list using sorting function
    def iterate(self):
        return self.sortingFunc(self.sequence)


# driver code
listOfNums = [3213213123, -32131, 2313, 0 ,32, -23, 65, -685, 534, 0, -90]
obj = IterableSort(bubble_sort, listOfNums)

print(listOfNums)
for seq in obj.iterate():
     print(seq)