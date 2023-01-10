class BST_Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    # Insert method to create nodes
    def insert(self, key):
        if key <= self.key:
            if self.left is not None:
                self.left.insert(key)
            else:
                self.left = self.left.insert(key) if self.left else BST_Node(key)
        else:
            if self.right is not None:
                self.right.insert(key)
            else:
                self.right = self.right.insert(key) if self.right else BST_Node(key)

    # Delete method to delete nodes based on key
    def delete(self, key):

        if key > self.key:
            self.right = self.right.delete(key) if self.right else None
        elif key < self.key:
            self.left = self.left.delete(key) if self.left else None
        else:
            # Leaf Node
            if (self.left is None) and (self.right is None):
                return None
            # Only Left Descendant is Present
            elif self.left and (self.right is None):
                replacement_node = self.left
                self.left = None
                return replacement_node
            # Only Right Descendant is Present
            elif self.right and (self.left is None):
                replacement_node = self.right
                self.right = None
                return replacement_node
            # Both Descendants are present
            parent = self
            child = self.right
            while child.left is not None:
                parent = child
                child = child.left
            # Edge Case: Parent is self.
            # Only One Depth it went. While Loop never Ran
            if parent == self:
                parent.right = child.right
            else:
                parent.left = child.right
            child.right = None
            self.key = child.key
            return self

        return self

    # Find method to compare the value with nodes
    def find(self, lkpkey):
        if lkpkey == self.key:
            return True
        if (lkpkey <= self.key) and (self.left is not None):
            return self.left.find(lkpkey)
        if (lkpkey > self.key) and (self.right is not None):
            return self.right.find(lkpkey)
        return False

    # Print the tree in order
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.key)
        if self.right:
            self.right.PrintTree()
