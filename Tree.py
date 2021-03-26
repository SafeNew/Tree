class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def __str__(self):
        return f"[{self.key}],[{self.left_child}],[{self.right_child}]"


Tree = BinaryTree("*")
Tree.insert_left("+")
Tree.insert_right("+")
Tree.left_child.insert_left("7")
Tree.left_child.insert_right("3")
Tree.right_child.insert_left("5")
Tree.right_child.insert_right("2")
# print(Tree.right_child.right_child)
# print(Tree)


def isOperator(x):
    if x == "+":
        return True
    elif x == "-":
        return True
    elif x == "*":
        return True
    elif x == "/":
        return True
    else:
        return False


def calculateTree(Tree):
    if type(Tree) != BinaryTree:
        raise ValueError
    if isOperator(Tree.key):
        left = calculateTree(Tree.left_child)
        print(left)
        right = calculateTree(Tree.right_child)
        print(right)
        if Tree.key == "+":
            Tree.key = left + right
        elif Tree.key == "-":
            Tree.key = left - right
        elif Tree.key == "*":
            Tree.key = left * right
        elif Tree.key == "/":
            if right == 0:
                raise ZeroDivisionError
            Tree.key = left / right
        return Tree.key
    elif Tree.key == None:
        return
    else:
        return int(Tree.key)


print(Tree)
print(calculateTree(Tree))
