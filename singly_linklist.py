
# each node of singly link list will contain value and pointer to the next node

class singly_node:
    def __init__(self, data):
        self.value = data
        self.next = None
        
class SinglylinkList:
    def __init__(self):
        self.head = None
    
    def insert_at_tail(self, data):
        new_node = singly_node(data)
        # if the list is empty insert the node as head
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            # find the last node
            while temp.next != None:
                temp = temp.next
            # add the node to the last node   
            temp.next = new_node
                
            
    def insert_at_head(self, data):
        new_node = singly_node(data)
        
        # if the list is empty
        if self.head == None:
            self.head = new_node
        else:
            # add the head node in the next of the new node and make the new node new head
            new_node.next = self.head
            self.head = new_node
        
    def insert_node(self, data, position):
        #create a node
        new_node = singly_node(data)
        # if the position is head
        if position == 0:
            self.insert_at_head(data)
            return
        
        #start with node 1
        i = 1
        # track the node before the given index and the node currently at the index
        prev_node = self.head
        curr_node = prev_node.next
        
        # search for the index till the last node
        while curr_node != None:
            if i == position:
                break
            prev_node = curr_node
            curr_node = curr_node.next
            i+=1   
                
        # if the position is not found till tail
        else:
            # if the position is tail_index +1
            if i == position:
                self.insert_at_tail(data)
            else:
                print("please provide the valid index")
            return
        # assign current node to the next of new_node  
        new_node.next = curr_node
        # add new_node to the next of prev_node
        prev_node.next = new_node       
                
            
        
    def print_linked_list(self):
        x = self.head
        while x != None:
            yield x.value
            x = x.next
        
    def delete_node(self, key):
        temp = self.head
        
        # if node to be deleted is head
        if temp.value == key:
            self.head = temp.next
            return
        
        prev = temp
        temp = temp.next
        
        # loop till the last element of the link list
        while temp != None:
            # if the element found then break
            if temp.value == key:
                break
            prev = temp
            temp = temp.next
         # if not found
        else:
            print("key not found")
            return
        #if found
        prev.next = temp.next
            
    def deleteHead(self):
        # if link list is not empty
        if self.head != None:
            self.head = self.head.next
        #otherwise
        else:
            print("Link List is empty")
            
    def deleteTail(self):
        # if link list is not empty
        if self.head != None:
            # initialize the temp by head
            Temp = self.head
            # stop the loop at the tail
            while Temp.next != None:
                prev = Temp
                Temp = Temp.next
            # if the list has more than one element
            try:
                prev.next = None
            # if it has only one elememt
            except:
                self.head = None
                print("your List is empty now")
                
        else:
            print("List is empty")