# from typing import Iterable
# from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
# from socket import INADDR_ALLHOSTS_GROUP
# from errno import ENOENT
#import itertools


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        newNode = Node(data, self.head)
        if self.head is None:
            self.head = newNode
            return

        self.head.prev = newNode
        self.head = newNode

    def printForward(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        dllStr = ""
        itr = self.head
        while itr:
            dllStr += str(itr.data) + "-->"
            itr = itr.next
        print("Linked list in forward fashion:- ", dllStr)

    def printReverse(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        itrble = self.head
        while itrble.next:
            itrble = itrble.next

        revstr = ""
        while itrble:
            revstr += str(itrble.data) + "-->"
            itrble = itrble.prev
        print("Linked list in reverse fashion:- ", revstr)

    def insertAtEnd(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        newNode = Node(data, None, itr)
        itr.next = newNode

    def insertValues(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtEnd(data)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")

        if index == 0:
            if self.head is None:
                raise Exception("Linked list is empty.")
            self.head = self.head.next
            return

            count = 0
            itr = self.head
            while itr:
                if itr.next is None:
                    raise Exception("Invalid index.")
                if count == index - 1:
                    if index is self.getLength() - 1:
                        itr.next = None
                        break
                    # the remove at end can be handeled  by the one below
                    itr.next = itr.next.next
                    itr.next.next.prev = itr
                    break
                itr = itr.next
                count += 1

    def insertAt(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.insertAtBegining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                node.prev = itr
                break

            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = DoublyLinkedList()
    #ll.insertValues(["banana", "mango", "grapes", "orange"])
    #ll.printForward()
    #ll.printReverse()
    #ll.insertAtEnd("figs")
    #ll.printForward()
    ll.insertValues(["banana","mango","grapes","orange"])
    ll.printForward()
    ll.printReverse()
    ll.insertAtEnd("figs")
    ll.printForward()
    ll.insertAt(0,"jackfruit")
    ll.printForward()
    ll.insertAt(6,"dates")
    ll.printForward()
    ll.insertAt(2,"kiwi")
    ll.printForward()