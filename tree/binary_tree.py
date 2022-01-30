#
#  Created By: Mohinish Joshi on 30/01/22, 7:50 PM
#
from tree.print_tree import printTree
from tree.tree_node import TreeNode
from tree.tree_traversal import *


class BinaryTree:
    def __init__(self, rootVal=None):
        self.root = rootVal

    def print(self):
        printTree(self.root)

    def search(self, value):
        if not self.root:
            return "Not Found"
        queue = []
        queue.append(self.root)
        valueFound = False
        while len(queue) > 0:
            root = queue.pop(0)

            if value == root.value:
                valueFound = True
                break
            if root.left:
                queue.append(root.left)
            if root.left:
                queue.append(root.right)

        return valueFound

    def insert(self, value):
        newNode = TreeNode(value)
        if not self.root:
            self.root = newNode

        queue = [self.root]
        while len(queue) > 0:
            root = queue.pop(0)
            if not root.left:
                root.left = newNode
                break
            else:
                queue.append(root.left)

            if not root.right:
                root.right = newNode
                break
            else:
                queue.append(root.right)

    @classmethod
    def create(cls):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)
        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)
        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        tree = BinaryTree(root)
        return tree


tree = BinaryTree.create()
tree.print()
print("Search Result:", tree.search(10))
print("Search Result:", tree.search(1))
print("Search Result:", tree.search(50))
tree.insert(50)
print("Search Result:", tree.search(50))
tree.print()

# print("\n-------------- In-Order --------------")
# tree.print()
# inorder(tree.root)
# print("\n-------------- Pre-Order --------------")
# tree.print()
# preorder(tree.root)
# print("\n-------------- Post-Order --------------")
# tree.print()
# postorder(tree.root)
# print("\n-------------- Level-Order --------------")
# tree.print()
# levelorder(tree.root)
