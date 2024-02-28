# explanations for member functions are provided in requirements.py
from __future__ import annotations

class FibNodeLazy:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False
        self.vacant = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNodeLazy):
        return self.val == other.val

class FibHeapLazy:
    def __init__(self):
        # you may define any additional member variables you need
        self.min = None
        self.roots = []

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNodeLazy:
        node = FibNodeLazy(val)
        self.roots.append(node)
        if self.min is None:
            self.min = node
        elif node.val < self.min.val:
            self.min = node
        return node

    def delete_min_lazy(self) -> None:
        self.min.vacant = True

    def dfs(self, node: FibNodeLazy):
        for child in node.children:
            if not child.vacant:
                child.flag = False
                self.roots.append(child)
            else:
                self.dfs(child)

    def find_min_lazy(self) -> FibNodeLazy:
        # 1 - break all the subtrees of vacant node and add it to the root
        for node in self.roots:
            if node.vacant:
                self.dfs(node)
                self.roots.remove(node)

        # 2 - merge the list based on delete min from basic fHeap
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

        # 3 - create root array and find min
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
        
        return self.min
   
    def cut_nodes(self, node: FibNodeLazy):
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

    def decrease_priority(self, node: FibNodeLazy, new_val: int) -> None:
        node.val = new_val
        if node.val < self.min.val:
            self.min = node
        if node.parent is None or node.parent.val < new_val:
            return
        self.cut_nodes(node)

    def dfsPrint(self, node: FibNodeLazy):
        print(node.val, " : ", node.flag)
        for child in node.get_children(): 
            self.dfsPrint(child)

    def print_fib(self):
        for root_child in self.roots:
            print("------")
            self.dfsPrint(root_child)
        print("====================", [child.val for child in self.roots])

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define