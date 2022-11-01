class node:
    def __init __ (self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly Linked list:
    def __init __(Self):
        self.first=None
        self.last=None
    def get_node(self,index):
        current=self.first
        for i in range (index):
            if current is None:
                return None
            current=current.next
            return current
    def insert_after(self,ref_node,new_node):
        new_node.prev=ref_node
        if ref_node.next is      None:
            self.last=new_node
        else:
            new_node.next=ref_node.next
            new_node.next=prev_new_node
        ref_node.next=new_node
    def insert_before(self,ref_node,new_node):
        new_node.next=ref_node
        if ref_node.prev is None:
            self.first=new_node
        else:
            new_node.prev=ref_node.prev
            new_node.prev.next=new_node
        ref_node.prev=next_node
    def insert_at_beg(self,new_node):
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.insert_before(self.first,new_node)
    def insert_at_end(self,new_node):
        if self.last is None:
           self.last=new_node
           self.first=new_node
        else:
            self.insert_after(self.last,new_node)
    def remove(self,node):
        if node.prev is None:
           self.first=node.next
        else:
            node.prev.next=node.next
        if node.next is None:
            self.last=node.prev
        else:
            node.next.prev=node.prev
    def display(self):
        current=self.first
        whilecurrent:
            print(current,data,end='')
            current=current.next
    a_dlist=Doubly Linked list()
    print('menu')
    print('insert<data>after<index>')
    print('insert<data>before<index')
    print('insert<data>at beg')
    print('insert<data>at end')
    print('remove<index>')
    print('quit')
    while true:
        print('the list:',end='')
        a_dlist.display()
        print()
        do=input("what would you like to do?").spilt()
        operation =do[0].strip.lower()
        if operation==;'insert':
            data=int(do[1])
            position=do[3].strip().lower()
            new_node=Node(data)
            suboperation=='at':
                If suboperation=do[2].strip().lower()
                If position=='beg'
                
            
          
        































































































































































































































































































































































































































































































































































































            
    
               
        
                                                                                                                                                        
