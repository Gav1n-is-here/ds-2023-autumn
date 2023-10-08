class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class linkList(object):
    """单链表"""
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def length(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.item)
            cur = cur.next
 
    def add(self, item):
        node = SingleNode(item)
        node.next = self.head
        self.head = node
 
    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self.head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
 
    def remove(self, item):
        cur = self.head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
 
    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

list1 = linkList()
list1.add(1)
list1.add(2)
list1.append(3)
print("length:",list1.length())
list1.travel()
print(list1.search(3))
print(list1.search(5))
list1.remove(1)
print("length:",list1.length())
list1.travel()