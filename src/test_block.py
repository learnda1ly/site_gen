from block import BlockType, block_to_blocktype
from block_markdown import markdown_to_blocks
import unittest


class testMarkdownBlock(unittest.TestCase):
    def test_block_paragraph(self):
        input = """
this is a paragraph
"""
        [block] = markdown_to_blocks(input)
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_block_header(self):
        input = """
#this is a heading
"""
        [block] = markdown_to_blocks(input)
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_block_code(self):
        input = """
```
this is a code block
```
"""
        [block] = markdown_to_blocks(input)
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.CODE)

    def test_block_quote(self):
        input = """
>this is a quote block
>with multiple lines for good measure
"""
        [block] = markdown_to_blocks(input)
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_block_unordered_list(self):
        input = """
- this is an unordered list item
- this is another item in an unordered list
"""
        [block] = markdown_to_blocks(input)
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_block_ordered_list(self):
        input = """
1. this is an ordered list item
2. this is another item in an ordered list
"""
        [block] = markdown_to_blocks(input)
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

