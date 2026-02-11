from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_blocktype(block: str) -> BlockType:
    block = block.strip("\n")

    if block[0] == "#":
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    if lines[0].startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                raise Exception("something wrong with quote block")
        return BlockType.QUOTE

    if lines[0].startswith("-"):
        for line in lines:
            if not line.startswith("-"):
                raise Exception("something wrong with unordered_list block")
        return BlockType.UNORDERED_LIST

    if re.match(r"^\d\..*", lines[0]):
        regex = r"^\d\..*"
        for line in lines:
            if not re.match(regex, line):
                raise Exception("something wrong with ordered_list block")
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
