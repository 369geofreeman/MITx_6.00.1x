class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        newNode = node(data)
        currentNode = self.head
        while currentNode.next!=None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def length(self):
        currentNode = self.head
        total = 0
        while currentNode.next!=None:
            total+=1
            currentNode = currentNode.next
        return total

    def display(self):
        elements = []
        currentNode = self.head
        while currentNode.next!=None:
            currentNode = currentNode.next
            elements.append(currentNode.data)
        print(elements)

    def get(self,index):
        if index>=self.length() or index<0:
            print('ERROR: List index out of range!')
            return None
        currentIndex = 0
        currentNode = self.head

        while True:
            currentNode = currentNode.next
            if currentIndex == index:
                return currentNode.data
            else:
                currentIndex +=1


    def erase(self,index):
        if index>=self.length() or index<0:
            print('ERROR: List index out of range!')
            return None

        currentIndex = 0
        currentNode = self.head

        while True:
            lastNode = currentNode
            currentNode = currentNode.next
            if currentIndex == index:
                lastNode.next = currentNode.next
                return
            currentIndex +=1





myList = linked_list()

print(myList.display())

myList.append(420)
myList.append(69)
myList.append(369)
myList.append(6666600000)
print(myList.display())


print("Element at 2nd index: {}".format(myList.get(1)))
myList.erase(3)
print(myList.display())



