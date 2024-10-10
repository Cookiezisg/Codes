
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def list_to_tree(lst):
    if not lst:
        return None

    # 创建根节点
    root = Node(lst[0])
    queue = [root]
    i = 1

    # 使用队列进行层序遍历，构造二叉树
    while i < len(lst):
        current = queue.pop(0)  # 当前节点出队

        # 处理左子节点
        if i < len(lst) and lst[i] is not None:
            current.left = Node(lst[i])
            queue.append(current.left)
        i += 1

        # 处理右子节点
        if i < len(lst) and lst[i] is not None:
            current.right = Node(lst[i])
            queue.append(current.right)
        i += 1

    return root

# 将列表转化为二叉树
lst = [1, 2, 3, 4, 5, None, 7]
root = list_to_tree(lst)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        current = root
        while current:
            dummy = Node(0)
            tail = dummy



print(root.left.val)