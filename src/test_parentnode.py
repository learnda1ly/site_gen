import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_parentnode_missing_tag_raises_valueerror(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag=None, children=None)
            node.to_html()

    def test_parentnode_missing_children_raises_valueerror(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag=None, children=None)
            node.to_html()

    def test_parentnode_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
