# stack using singly link list which perform pop() and push() in O(1) time

# --------------------stack----------------

class stack_node:
    """create the node for stack"""
    def __init__(self, data):
        self.key = data
        self.next = None
        
class stack:
    
    def __init__(self):
        """ create the empy stack"""
        self.head = None
        
    def push(self, data):
        """push the data to the head"""
        new_node = stack_node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        """ pop the data from head"""
        try:
            x = self.head.key
            self.head = self.head.next
            return x
        except:
            print("stack is empty")
            
    def print_stack(self):
        """print the stack"""
        s = self.head
        if s != None:
            while s != None:
                yield s.key
                s = s.next
        else:
            print("stack is empty")
            
# ------------------- Queue -----------------

class q_node:
    def __init__(self, data):
        """Create the node for queue"""
        self.value = data
        self.next = None
class Queue:
    def __init__(self):
        """creates the empty queue"""
        self.head = None
        self.tail = None
        
    def enqueue(self, data):
        """ add the new node to the queue at the tail"""
        new_node = q_node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def dequeue(self):
        """ remove the node from the head"""
        data = self.head.value
        self.head = self.head.next
        return(data)
        
    def print_queue(self):
        """ Print the queue"""
        h = self.head
        while h != None:
            yield h.value
            h = h.next
            
            