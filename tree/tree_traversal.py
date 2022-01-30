#
#  Created By: Mohinish Joshi on 30/01/22, 8:55 PM
#
from queue.QueueWithLinkedList import QueueWithLinkedList


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.value)
    inorder(root.left)
    inorder(root.right)


def postorder(root):
    if not root:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.value)


def levelorder(root):
    if not root:
        return
    else:
        queue = []

        # Enqueue Root and initialize height
        queue.append(root)
        while len(queue) > 0:
            print(queue[0].value)
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

