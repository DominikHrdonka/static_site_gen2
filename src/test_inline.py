import unittest
from textnode import TextNode, TextType
from inline import split_node_delimiter


class TestInlineNode(unittest.TestCase):

    def test_split_node_delimiter_BOLD(self):
        node = TextNode("This is a **bold** word and this is not.", TextType.TEXT)
        new_nodes = split_node_delimiter(node, '**', TextType.BOLD)
        final_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and this is not.", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, final_nodes)
        