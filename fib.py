# explanations for member functions are provided in requirements.py
from __future__ import annotations

class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.min = None
        self.roots = []

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        node = FibNode(val)
        self.roots.append(node)
        if self.min is None:
            self.min = node
        elif node.val < self.min.val:
            self.min = node
        return node

    def delete_min(self) -> None:
        # 1. copy children of min in root -> set their flags to false
        # 2. clean up - merge node with similar degree
        # 3. find min and update roots.

        # 1.
        for child in self.min.get_children():
            child.parent = None
            self.roots.append(child)
            child.flag = False
        self.roots.remove(self.min)

        # 2.
        degree_map = {}
        for node in self.roots:
            degree = len(node.children)
            while degree_map.get(degree) is not None:
                old_node = degree_map.pop(degree)
                if node.val > old_node.val:
                    node.parent = old_node
                    old_node.children.append(node)
                    node = old_node
                else:
                    old_node.parent = node
                    node.children.append(old_node)
                degree += 1
            degree_map[degree] = node
    
        # 3. 
        self.roots = []
        for value in degree_map.values():
            if value is not None:
                self.roots.append(value)

        self.min = None
        for value in self.roots:
            if self.min is None:
                self.min = value
            elif value.val < self.min.val:
                self.min = value

    def find_min(self) -> FibNode:
        return self.min
    
    def cut_nodes(self, node: FibNode):
        parent = node.parent
        node.flag = False
        node.parent = None

        if node.val < self.min.val:
            self.min = node

        if parent is not None:
            parent.children.remove(node)
            self.roots.append(node)
            if parent.flag:
                self.cut_nodes(parent)
            else:
                parent.flag = True

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val
        if node.val < self.min.val:
            self.min = node
        if node.parent is None or node.parent.val < new_val:
            return
        self.cut_nodes(node)

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define