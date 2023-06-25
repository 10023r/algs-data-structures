from typing import Union


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Union[Node, None] = left
        self.right: Union[Node, None] = right
        self.height: int = 1

    def __str__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return 'left: {}, mid: {}, right: {}'.format(left, self.val, right)