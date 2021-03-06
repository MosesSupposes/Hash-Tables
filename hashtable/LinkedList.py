class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
# What differentiates this Linked List from a regular Linked List is that this Linked List uses "HashTableEntries" as its nodes

class HashedLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 1 if head else 0
    
    def add_to_head(self, key, value):
        if self.head is None:
            self.head = HashTableEntry(key, value)
            self.tail = self.head
        else:
            old_head = self.head
            self.head = HashTableEntry(key, value)
            self.head.next = old_head 
    
    def add_to_tail(self, key, value):
        """
        The ceremony of finding the tail isn't necessary since it's made available in the constructor,
        but I decided to do it this way anyways for practice.
        """
        def find_tail(node):
            if node.next is None:
                return node
            else: 
                return find_tail(node.next)

        if self.head is None:
            self.head = HashTableEntry(key, value)
            self.tail = self.head 
            self.size += 1
            return 
        else:
            tail = find_tail(self.head)
            n = HashTableEntry(key, value)  
            tail.next = n
            n.next = None
            self.tail = n
            self.size += 1
        
    def find_node(self, key):
        def look_until_found(node):
            if node is None:
                return None
            elif node.key == key:
                return node
            else:
                return look_until_found(node.next)

        return look_until_found(self.head)
    
    def update_node(self, key, value):
        node_to_update = self.find_node(key)
        if node_to_update is not None:
            node_to_update.value = value
        else:
            return None

    def remove_node(self, key):
        cur = self.head
        prev = "null" 

        # Finds the node before the node to delete
        def find_previous_node(prev, cur):
            if cur.key == key:
                return prev 
            elif cur is None:
                return None
            else:
                return find_previous_node(cur, cur.next)
            
        previous_node = find_previous_node(prev, cur)
        if previous_node is not None and previous_node != "null":
            previous_node.next = previous_node.next.next
            self.size -= 1
            return 1 
        # If the key to remove is the head of the list...
        elif previous_node == "null":
            self.head = self.head.next
            self.size -= 1
            return 1
        else:
            return 0
    
    def for_each(self, cb):
        def recur(node):
            if node is None:
                return
            cb(node)
            recur(node.next)

        recur(self.head)





