def main():
    # We'll define the class ListMap
    map = ListMap()
    # It works similar to Linked List and every key value pair is a node of the list
    # Every new node is added to the end  of the list

    # Keys are unique in the dictionary
    map.put("Name", "Sam")
    map.put("City", "Delhi")
    map.put("City", "Pune") # Delhi will be erased and Pune will be replaced

    print(map.get("City"))


class Node:
    def __init__(self, key=None, value=None): # default arguments
        self.key = key
        self.value = value
        self.next = None


class ListMap:
    def __init__(self):
        self.head = None

    def put(self, key, value):
        if self.head == None:
            node = Node(key, value)
            self.head = node
        else:
            temp = self.head
            while temp.next != None and temp.key != key:
                temp = temp.next
            if temp.key == key: # if the key is found , then edit the value
                temp.value = value
            else:                # when we have a new key value pair then add a node to end
                node = Node(key, value)
                temp.next = node

    def get(self, key):
        temp = self.head
        while temp != None: # we also has to access the last node for temp.value therefore temp != None
            if temp.key == key:
                return temp.value
            temp = temp.next
        return None


if __name__ == "__main__":
    main()