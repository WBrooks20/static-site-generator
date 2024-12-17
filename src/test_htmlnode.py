import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode()
        html_node.props = {"href": "https://www.google.com", "target": "_blank"}
        self.assertEqual(html_node.props_to_html(),' href="https://www.google.com" target="_blank"')
    def test_props_to_html_two(self):
        html_node = HTMLNode()
        html_node.props = {
            "href1": "google.com",
            "target1": "google",
            "href2": "skype.com",
            "target2": "skype",
            "href3": "boot.dev",
            "target3": "bootdev"
        }   
        self.assertEqual(html_node.props_to_html(),' href1="google.com" target1="google" href2="skype.com" target2="skype" href3="boot.dev" target3="bootdev"')
    def test_props_to_html_three(self):
        html_node = HTMLNode()
        html_node.props = {"test":"123"}
        self.assertEqual(html_node.props_to_html(),' test="123"')
if __name__ == "__main__":
    unittest.main()