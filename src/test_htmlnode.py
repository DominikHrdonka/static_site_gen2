import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), string)

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"src": "images/profile.jpg", "alt": "Profile picture", "width": "100"})
        string = ' src="images/profile.jpg" alt="Profile picture" width="100"'
        self.assertEqual(node.props_to_html(), string)
    
    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        string = ""
        self.assertEqual(node.props_to_html(), string)

    def test_props_to_html_none(self):
        node = HTMLNode()
        string = ""
        self.assertEqual(node.props_to_html(), string)

    #Testing LeafNode methods

    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        final_string = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), final_string)
    
    def test_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        final_string = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), final_string)
    
    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just a raw text.")
        final_string = "Just a raw text."
        self.assertEqual(final_string, node.to_html())

    #Testing ParentNode methods

    def test_to_html_one_child(self):
        node = ParentNode("p", [LeafNode("b", "This is a bold text.")])
        final_string = "<p><b>This is a bold text.</b></p>"
        self.assertEqual(final_string, node.to_html())
    
    def test_to_html_multiple_children(self):
        node = ParentNode("div", [ParentNode("section", [LeafNode("p", "This is a paragraph inside a section."), LeafNode("p", "Another paragraph in the same section.")]), ParentNode("footer", [LeafNode("p", "This is a paragraph in the footer.")])])
        final_string = "<div><section><p>This is a paragraph inside a section.</p><p>Another paragraph in the same section.</p></section><footer><p>This is a paragraph in the footer.</p></footer></div>"
        self.assertEqual(final_string, node.to_html())

    def test_missing_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("b", "This is a bold text.")])
        error_message = "Tag is required."
        self.assertEqual(str(context.exception), error_message)

    def test_empty_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("", [LeafNode("b", "This is a bold text.")])
        error_message = "Tag is required."
        self.assertEqual(str(context.exception), error_message)

    def test_empty_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p", [])
        error_message = "Children cannot be empty."
        self.assertEqual(str(context.exception), error_message)
    
    def test_children_wrong_type(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p", 'LeafNode("b", "This is a bold text.")')
        error_message = "Children must be a list."
        self.assertEqual(str(context.exception), error_message)

    def test_missing_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p", None)
        error_message = "Children are required."
        self.assertEqual(str(context.exception), error_message)

    def test_children_descendancy(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [TextNode("This a text node", TextType.BOLD, "https://www.ahoj.com")])
        error_message = "Children must be an HTMLNode descendant."
        self.assertEqual(str(context.exception), error_message)
    
    
    
    