class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


class PriorityNode:
    def __init__(self, data, priority):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return str(self.data)


class PriorityQueue:
    def __init__(self):
        self.data = BinHeap()

    def enqueue(self, item, priority):
        self.data.insert(PriorityNode(item, priority))

    def dequeue(self):
        return self.data.delMin().data


pq = PriorityQueue()

pq.enqueue("prior 1", 1)
pq.enqueue("prior 3", 3)
pq.enqueue("prior 2", 2)
pq.enqueue("prior 4", 4)

print(pq.data.heapList)
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())