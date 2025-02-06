import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This a text node", TextType.BOLD, "https://www.ahoj.com")
        node2 = TextNode("This a text node", TextType.BOLD, "https://www.ahoj.com")
        self.assertEqual(node, node2)

    def test_noteq_type(self):
        node = TextNode("This a text node", TextType.BOLD)
        node2 = TextNode("This a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_noteq_text(self):
        node = TextNode("This a text node", TextType.BOLD)
        node2 = TextNode("This a different node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq_url(self):
        node = TextNode("This a text node", TextType.BOLD, "https://www.ahoj.com")
        node2= TextNode("This a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    #Testing text_node_to_html():
    def test_text_node_to_html_TEXT(self):
        node = TextNode("This is a paragraph", TextType.TEXT)
        html_node = LeafNode(None, "This is a paragraph")
        self.assertEqual(text_node_to_html_node(node), html_node)

    def test_text_node_to_html_BOLD(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        html_node = LeafNode("b", "This is a bold text")
        self.assertEqual(text_node_to_html_node(node), html_node)

    def test_text_node_to_html_ITALIC(self):
        node = TextNode("This is an italic text", TextType.ITALIC)
        html_node = LeafNode("i", "This is an italic text")
        self.assertEqual(text_node_to_html_node(node), html_node)

    def test_text_node_to_html_node_CODE(self):
        node = TextNode("This is a code", TextType.CODE)
        html_node = LeafNode("code", "This is a code")
        self.assertEqual(text_node_to_html_node(node), html_node)

    def test_text_node_to_html_node_LINK(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.ahoj.com")
        html_node = LeafNode("a", "This is a link", {"href": "https://www.ahoj.com"})
        self.assertEqual(text_node_to_html_node(node), html_node)
    
    def test_text_node_to_html_node_IMAGE(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.image.com")
        html_node = LeafNode("img", "", {"src": "https://www.image.com", "alt":"This is an image"})
        self.assertEqual(text_node_to_html_node(node), html_node)
    
    def test_text_node_to_html_node_INVALID(self):
        node = TextNode("Invalid text type", TextType.TEXT)
        node.text_type = "invalid_type"
        with self.assertRaises(TypeError) as context:
            text_node_to_html_node(node)
        error_message = "Not supported text type."
        self.assertEqual(str(context.exception), error_message)

    def test_text_node_to_html_node_INVALID2(self):
        node = TextNode("This is also an invalid text type", TextType.BOLD)
        node.text_type = "invalid_type_again"
        with self.assertRaises(TypeError) as context:
            text_node_to_html_node(node)
        error_message = "Not supported text type."
        self.assertEqual(str(context.exception), error_message)

        
        


if __name__ == "__main__":
    unittest.main()