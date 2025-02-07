from textnode import TextType, TextNode
def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            node.text.split(delimiter)
        else:
            new_nodes.extend(node)
        