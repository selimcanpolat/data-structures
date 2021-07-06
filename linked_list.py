class Node:

    def __init__(self,data=None,next=None):
        self.data = data # data inside the node
        self.next = next # the pointer from the current node to the next node

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        return count

    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        iterator = self.head
        llstr = ""
        count = 0
        while iterator:
            count += 1
            if self.get_length() == count:
                llstr += str(iterator.data)
                break
            llstr += str(iterator.data) + " --> "
            iterator = iterator.next
        print(llstr)

    def append(self,data):

        if self.head is None: # if the linked list was empty
            self.head = Node(data,None)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data,None)

    def insert_values(self,data_list):
        #self.head = None
        for data in data_list:
            self.append(data)


    def remove_at(self,index):

        if index<0 or index > self.get_length(): # validating the index
            raise Exception("Index out of range")

        if index == 0: # if we're trying to remove the head (the first node)
            self.head = self.head.next
            return

        count = 0
        iterator = self.head
        while iterator:
            count += 1
            if count == index:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next

    def insert_at(self,index,data):

        if index<0 or index > self.get_length(): # validating the index
            raise Exception("Index out of range")

        if index == 0:
            self.insert_at_the_beginning(data)
            return

        count = 0
        iterator = self.head
        while iterator:
            if count == index-1:
                node = Node(data,iterator.next)
                iterator.next = node
                return
            count += 1
            iterator = iterator.next

ll = LinkedList()
ll.insert_values([2,3,4,5,6,7,11,2,"ab","cde"])
ll.insert_at(9,"figs")
ll.print()

