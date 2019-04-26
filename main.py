from arrayheap import *

def simpleHeapSort(theSeq):
    # Create an array-based max-heap.
    n = len(theSeq)
    heap = MaxHeap(n)

    # Build a max-heap from the list of values.
    for item in theSeq:
        heap.add(item)
    
    # Extract each value from the heap and store the back into the list.
    for i in range(n-1, -1, -1):
        theSeq[i] = heap.extract()

f = open("words_15.txt", "r")
simpleList = []
contents = f.readlines()

for item in contents:
    simpleList.append(item)
simpleHeapSort(simpleList)

w = open("sorted_words_15.txt", "w+")
for item in simpleList:
    w.write(item)
f.close()
w.close()
