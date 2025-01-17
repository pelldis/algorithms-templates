# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, elem):
    # Your code
    # ヽ(´▽`)/
    idx = 0
    if node.value == elem:
        return 0
    next_node = node.next_item
    while next_node is not None:
        idx += 1
        value = next_node.value
        if value == elem:
            return idx
        next_node = next_node.next_item
    return - 1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__':
    test()
