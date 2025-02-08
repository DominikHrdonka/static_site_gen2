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
        
    def test_split_node_delimiter_ITALIC(self):
        node = TextNode("This is a *italic* text and this is not.", TextType.TEXT)
        new_nodes = split_node_delimiter(node, '*', TextType.ITALIC)
        final_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text and this is not.", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, final_nodes)

    def test_split_node_delimiter_CODE(self):
        node = TextNode("This is a `code` and this is not", TextType.TEXT)
        new_nodes = split_node_delimiter(node, '`', TextType.CODE)
        final_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and this is not", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, final_nodes)

    def test_split_node_delimiter_NOT_TEXT(self):
        node = TextNode("This is an invalid node", TextType.BOLD)
        new_nodes = split_node_delimiter(node, '**', TextType.BOLD)
        final_nodes = [
            TextNode("This is an invalid node", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, final_nodes)

    def test_split_node_delimiter_INVALID_FORMATTING(self):
        node = TextNode("This is invalid **formatting of the text.", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            new_nodes = split_node_delimiter(node, '**', TextType.BOLD)
        error_message = "Improper delimiter formatting."
        self.assertEqual(str(context.exception), error_message)
            