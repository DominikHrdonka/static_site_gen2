from textnode import TextType, TextNode
def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in [old_nodes]:
        if node.text_type == TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Improper delimiter formatting.")
            else:
                for index, item in enumerate(split_text):
                    if index % 2 == 1:
                        new_nodes.append(TextNode(item, text_type))
                    else:
                        new_nodes.append(TextNode(item, TextType.TEXT))
                        
        else:
            new_nodes.append(TextNode(node.text, node.text_type))
            
    return new_nodes
        