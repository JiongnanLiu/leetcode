class ListNode:
    
    def __init__(self, key, value, node):
        self.val = [key, value]
        self.next = node

class LList:
    def __init__(self, key, value, nxt=None):
        self.head = ListNode(key, value, nxt)
        
    
    def get(self, key):
        temp = self.head
        if not temp:
            return -1
        
        while temp:
            if temp.val[0] == key:
                return temp.val[1]
            temp = temp.next
        return -1
    
    def remove(self, key):
        temp = self.head
        if not temp:
            return None
        while temp:
            if temp.val[0] == key:
                temp.val[1] = -1
            temp = temp.next
        return None
    
    def put(self, key, value):
        temp = self.head
        to_insert = ListNode(key, value, None)
        if not temp:
            temp = to_insert
            return None
        while temp.next:
            if temp.val[0] == key:
                temp.val[1] = value
                return None
            temp = temp.next
        if temp.val[0] == key:
            temp.val[1] = value
            return None
        else:
            temp.next = to_insert
        return None
        
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = [LList(i,-1, None) for i in range(1000)]
        
        

    def put(self, key, value):
        x = key % 1000
        node = self.d[x]
        node.put(key, value)
        return None
        

    def get(self, key) :

        x = key % 1000
        to_find = self.d[x]
        res = to_find.get(key)
        return res
        

    def remove(self, key):
        x = key % 1000
        to_remove = self.d[x]
        to_remove.remove(key)
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)