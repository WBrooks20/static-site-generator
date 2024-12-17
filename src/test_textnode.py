import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_upper_lower(self):
        node = TextNode("NewNode",TextType.Normal)
        node2 = TextNode("NewNode",TextType.Normal)
        self.assertEqual(node,node2)
    def test_url_none(self):
        node = TextNode("NewNode!",TextType.Code)
    def test_type_eq(self):
        node = TextNode("Node",TextType.BOLD,"www.www.com")
        node2 = TextNode("Node",TextType.BOLD,"www.www.com")
        self.assertEqual(node,node2)
    def test_type_URL_eq(self):
        node = TextNode("Node",TextType.BOLD,"www.com")
        node2 = TextNode("Node",TextType.BOLD,"www.com")
        self.assertEqual(node,node2)
if __name__ == "__main__":
    unittest.main()