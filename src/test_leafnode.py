import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode(
            "a", "This is a test", {"href": "www.google.com", "target": "_blank"}
        )

        self.assertEqual(
            node.to_html(),
            '<a href="www.google.com" target="_blank">This is a test</a>',
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_plain(self):
        node = LeafNode(None, "Plain Text")
        self.assertEqual(node.to_html(), "Plain Text")

    def test_leaf_raises_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None)
            node.to_html()


if __name__ == "__main__":
    unittest.main()
