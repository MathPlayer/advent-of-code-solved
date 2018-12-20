#!/usr/bin/env python3


def read_node(data):
    """Returns (node, unused_data)."""
    children = []
    metadata = []
    children_count = data[0]
    metadata_count = data[1]

    unused_data = data[2:]
    for _ in range(children_count):
        (node, unused_data) = read_node(unused_data)
        children.append(node)

    return (
        {"children": children, "metadata": unused_data[:metadata_count]},
        unused_data[metadata_count:])


def sum_metadata(node):
    return sum(node["metadata"]) + sum(map(sum_metadata, node["children"]))


def node_value(node):
    if not node["children"]:
        return sum(node["metadata"])
    s = 0
    for m in map(lambda x: x - 1, node["metadata"]):
        if m < len(node["children"]):
            s += node_value(node["children"][m])
    return s


with open("08.in") as f_in:
    data = map(int, f_in.read().strip().split(" "))

(root, unused) = read_node(data)

print(sum_metadata(root))
print(node_value(root))
