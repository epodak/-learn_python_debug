class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 插入到链表头部
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 删除头部节点
    def delete_head_node(self):
        if self.head is not None:
            self.head = self.head.next

    # 在链表尾部插入新节点
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    # 删除尾节点
    def delete_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last_node = self.head
        while second_last_node.next.next:
            second_last_node = second_last_node.next
        second_last_node.next = None
