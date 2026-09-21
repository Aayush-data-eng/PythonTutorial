from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

    def front (self) :
        return self.buffer[-1]

# This one way of  solving this particular question, in this solution type we are to recogonise the pattern ie) After 1, the second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1. 

def binarySequence1 (num) :
    numbersQueue = Queue()
    numbersQueue.enqueue('1')

    for i in range (num) :
        front = numbersQueue.front()
        # print("   ", front)
        print(front)
        numbersQueue.enqueue(front + '0')
        numbersQueue.enqueue(front + '1')

        numbersQueue.dequeue()


#Another type, here we will manually calculate the binary representation on any given numeral input.

def binaryRepresentation (numeral) :
    binaryNum = ''
    while numeral :
        binaryNum += str(numeral%2)
        numeral //= 2

    binaryNum = binaryNum[::-1]
    return binaryNum

def binarySequence2 (numbers) :
    numberQueue = Queue ()
    for i in range(numbers + 1) :
        numberQueue.enqueue(binaryRepresentation(i))
        print(numberQueue.dequeue())

if __name__ == "__main__" :
    binarySequence1(10)
    print()
    binarySequence2(10)