import random
from typing import Union
from Node import Node


# def dfs(node):
#     if node:
#         left = dfs(node.left)
#         cur = [node.val]
#         right = dfs(node.right)
#         return left + cur + right
#     return []


class AVLTree:
    def __init__(self, val=None):
        self.root: Union[Node, None] = Node(val) if val else None

    def insert(self, val) -> None:
        self.root = self._insert_rec(val, self.root)

    def find(self, val) -> bool:
        node = self.root
        while node:
            if node.val == val:
                return True
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, val: int):
        self.root = self._remove_rec(val, self.root)

    def _insert_rec(self, val, node: Node) -> Node:
        if not node:
            node = Node(val)
        elif val < node.val:
            node.left = self._insert_rec(val, node.left)
        else:
            node.right = self._insert_rec(val, node.right)
        node = self._balance_node(node)
        return node

    def _small_right_rotation(self, node) -> Node:
        new_node = node.left
        node.left = new_node.right
        new_node.right = node
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        # new_node.height = max(self._get_height(new_node.left), self._get_height(new_node.right)) + 1
        return new_node

    def _small_left_rotation(self, node) -> Node:
        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        # new_node.height = max(self._get_height(new_node.left), self._get_height(new_node.right)) + 1
        return new_node

    def _remove_rec(self, val: int, node: Union[Node, None]) -> Union[Node, None]:
        if node is None:
            return node
        if val < node.val:
            node.left = self._remove_rec(val, node.left)
        elif val > node.val:
            node.right = self._remove_rec(val, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_max_val_node(node.left)
            node.val = temp.val
            node.left = self._remove_rec(temp.val, node.left)
        node = self._balance_node(node)
        return node

    def _balance_node(self, node) -> Node:
        balance = self._get_height_diff(node)
        if abs(balance) > 1:
            if balance < 0:  # rotate left
                if self._get_height(node.right.left) <= self._get_height(node.right.right):
                    node = self._small_left_rotation(node)
                else:
                    node.right = self._small_right_rotation(node.right)
                    node = self._small_left_rotation(node)
            else:
                if self._get_height(node.left.right) <= self._get_height(node.left.left):
                    node = self._small_right_rotation(node)
                else:
                    node.left = self._small_left_rotation(node.left)
                    node = self._small_right_rotation(node)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node

    def _get_height(self, node) -> int:
        if not node:
            return 0
        return node.height

    def _get_height_diff(self, node) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_max_val_node(self, node) -> Union[None, Node]:
        if node is None or node.right is None:
            return node
        return self._get_max_val_node(node.right)


avl_tree = AVLTree()
data_len = 10
test_data = [random.randint(0, 500) for _ in range(data_len)]
# test_data = [64, 293, 409, 245, 404, 483, 125, 356, 144, 281]
print(test_data)
for i in test_data:
    avl_tree.insert(i)
# res = dfs(avl_tree.root)
# print(res == sorted(res))
# for i in test_data:
#     avl_tree.remove(2)
# print(res)
