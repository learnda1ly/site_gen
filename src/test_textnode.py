import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_valid_eq(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_text_makes_neq(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is A text node", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_texttype_makes_neq(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)

        self.assertNotEqual(node, node2)

    def test_url_makes_neq(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is A text node", TextType.BOLD, "www.boot.dev")

        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
