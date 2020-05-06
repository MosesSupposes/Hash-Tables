from LinkedList import HashedLinkedList, HashTableEntry

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    # This is an fnv 32-bit hash
    def fnv1(self, key):
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for letter in key:
            hval = hval ^ ord(letter)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval

    # This is an fnv 64-bit hash
    def fnv164(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """
        str_bytes = str(key).encode()
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash = FNV_offset_basis
        for byte_of_data in str_bytes:
            hash = hash * FNV_prime
            hash = hash ^ byte_of_data
        hash &= 0xffffffffffffffff
        return hash

    def djb2(self, key):
        hash = 5381
        for letter in key:
            hash = (( hash << 5) + hash) + ord(letter)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the range of the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.fnv164(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # hll is short for "hashed_linked_list"
        hll = self.storage[self.hash_index(key)]
        if hll is None:
            # Create a Linked List and stuff it inside
            self.storage[self.hash_index(key)] = HashedLinkedList(HashTableEntry(key, value))
        else:
            # Append to the existing linked list if it's a new key, 
            # if it's an existing key, update the value of that node
            if hll.find_node(key) is None: 
                hll.add_to_tail(key, value)
            else:
                hll.update_node(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.storage[self.hash_index(key)] is None:
            print("Couldn't find the value stored at the given key")
        else:
            # Returns a 1 if successful or a 0 otherwise
            return self.storage[self.hash_index(key)].remove_node(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        linked_list = None
        try:
            linked_list = self.storage[self.hash_index(key)]
        except IndexError: 
            return None 
        else:
            if linked_list is None:
                return None
            else: 
                if linked_list.find_node(key) is not None:
                    return linked_list.find_node(key).value
                else:
                    return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
