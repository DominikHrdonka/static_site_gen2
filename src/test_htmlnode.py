import unittest

from htmlnode import HTMLNode

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