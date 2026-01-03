import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.node = HTMLNode(
            "a",
            "This is a test",
            None,
            {
                'href': 'www.google.com',
                'target': '_blank'
            }
        )

    def test_props_to_html(self):
        props_to_html = ' href="www.google.com" target="_blank"'
        self.assertEqual(self.node.props_to_html(), props_to_html)

    def test_repr(self):
        self.assertEqual(self.node.__repr__(
        ), "tag: a \nvalue: This is a test \nchildren: None \nprops: {'href': 'www.google.com', 'target': '_blank'}")


if __name__ == "__main__":
    unittest.main()
