class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        node = Node(data, self.head)
        self.head = node

    def printll(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head
        llstr = ""
        while temp:
            llstr += str(temp.data) + "-->"
            temp = temp.next
        print(llstr)

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

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
            raise Exception("Invalid Index.")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
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
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insertAfterValue(self, prevData, realData):
        if self.head is None:
            print("No such node present in linked list, ie) linked list is empty.")
            return
        if self.head.next is None:
            # This implies that we have only a single node
            if self.head.data == prevData:
                self.head.next = Node(realData)
            else:
                print("The provided data is not found in our list.")
            return

        itrble = self.head
        newNode = Node(realData)
        while itrble:
            if itrble.data == prevData:
                newNode.next = itrble.next
                itrble.next = newNode
                break

            itrble = itrble.next

    def removeByValue(self, data):
        if self.head is None:
            print(
                f"Our list is already empty, hence no such value like {data} ca nbe removed."
            )
            return

        if self.head.next is None:
            if self.head.data == data:
                self.head = None
            else:
                print(f"{data}, No such value present in our list.")
            return

        if self.head.data == data:
          self.head = self.head.next
      
        itrBle = self.head
        while itrBle.next:
            if itrBle.next.data == data:
                itrBle.next = itrBle.next.next
                break
            itrBle = itrBle.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertValues(["banana", "mango", "grapes", "orange"])
    ll.printll()
    ll.insertAfterValue("mango", "apple")  
    ll.printll()
    ll.removeByValue("orange") 
    ll.printll()
    ll.removeByValue("figs")
    ll.printll()
    ll.removeByValue("banana")
    ll.removeByValue("mango")
    ll.removeByValue("apple")
    ll.removeByValue("grapes")
    ll.printll()
