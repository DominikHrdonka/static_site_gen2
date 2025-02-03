import unittest

from htmlnode import HTMLNode, LeafNode

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