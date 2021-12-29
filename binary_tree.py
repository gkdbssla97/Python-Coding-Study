#binary tree

class Node:
    left = None
    right = None
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return f'node: {self.val}'
        #f-string
n1 = Node(10)
n2 = Node(5)
n1.left = n2
print(n1.left)
print(n1.right)
