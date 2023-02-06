class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())
    
    def inorder(self):
        return []
    
    def min_item(self):
        return None
    
    def max_item(self):
        return None
    
    def balance_factor(self):
        return None

    def balanced_everywhere(self):
        return True
    
    def add_to_all(self, add):
        return self
    
    def path_to(self, num):
        return None


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True
    
    def path_to(self, num):
        if not self.contains(num):
            print("does not contain")
            return None
        if self.value == num:
            return [self.value]
        if num < self.value:
            return [self.value] + self.left.path_to(num)
        return [self.value] + self.right.path_to(num)

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self
    
    def inorder(self):
        return self.left.inorder() + [self.value] + self.right.inorder()
    
    def min_item(self):
        if self.left.is_empty():
            return self.value
        return self.left.min_item()
    
    def max_item(self):
        if self.right.is_empty():
            return self.value
        return self.right.max_item()

    def balance_factor(self):
        return self.right.height() - self.left.height()

    def balanced_everywhere(self):
        return abs(self.balance_factor()) <= 1 and \
            (self.left.balanced_everywhere() and \
            self.right.balanced_everywhere())
    
    def add_to_all(self, add):
        return Node(self.value + add, 
                    self.left.add_to_all(add),
                   self.right.add_to_all(add) )


if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63).insert(95).add_to_all(1)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(f"Inorder: {bst.inorder()}")
    print(f"Min {bst.min_item()}")
    print(f"Max {bst.max_item()}")
    print(f"Balanced? {bst.balanced_everywhere()}")
    print(f"15path {bst.path_to(16)}")

