class Node:
    def __init__(self, value, color, left_child, right_child):
        self.value = value
        self.color = color
        self.left_child = left_child
        self.right_child = right_child


class r_b_tree():
    root = Node(None, None, None, None)

    def add(value):
        if r_b_tree.root.value != None:
            result = r_b_tree.add_node(r_b_tree.root, value)
            r_b_tree.root = rebalance(r_b_tree.root)
            r_b_tree.root.color = 'BLACK'
            return result
        else:
            r_b_tree.root = Node(value, 'BLACK', None, None)
            return True

    def add_node(node, value):
        if node.value == value:
            return False
        else:
            if node.value > value:
                if node.left_child != None:
                    result = r_b_tree.add_node(node.left_child, value)
                    node.left_child = rebalance(node.left_child)
                    return result
                else:
                    node.left_child = Node(value, 'RED', None, None)
                    return True
            else:
                if node.right_child != None:
                    result = r_b_tree.add_node(node.right_child, value)
                    node.right_child = rebalance(node.right_child)
                    return result
                else:
                    node.right_child = Node(value, 'RED', None, None)
                    return True


def color_swap(node):
    node.right_child.color = 'BLACK'
    node.left_child.color = 'BLACK'
    node.color = 'RED'


def left_swap(node):
    left_child = node.left_child
    between_child = left_child.right_child
    left_child.right_child = node
    node.left_child = between_child
    left_child.color = node.color
    node.color = 'RED'
    return left_child


def right_swap(node):
    right_child = node.right_child
    between_child = right_child.left_child
    right_child.left_child = node
    node.right_child = between_child
    right_child.color = node.color
    node.color = 'RED'
    return right_child


def rebalance(node):
    result = node
    need_rebalance = True
    while (need_rebalance == True):
        need_rebalance = False
        if result.right_child != None and result.right_child.color == 'RED' and (result.left_child == None or result.left_child.color == 'BLACK'):
            need_rebalance = True
            result = right_swap(result)
        if result.left_child != None and result.left_child.color == 'RED' and result.left_child.left_child != None and result.left_child.left_child.color == 'RED':
            need_rebalance = True
            result = left_swap(result)
        if result.left_child != None and result.left_child.color == 'RED' and result.right_child != None and result.right_child.color == 'RED':
            need_rebalance = True
            color_swap(result)
    return result


for i in range(1, 200):
    tree = r_b_tree.add(input())
    print(tree)
