from block import block_to_blocktype, BlockType
from htmlnode import ParentNode
from inline_markdown import text_to_text_nodes
from textnode import TextNode, text_node_to_html_node, TextType


def markdown_to_blocks(markdown: str):
    blocks = []
    for line in markdown.split("\n\n"):
        if line != "":
            blocks.append(line.strip("\n"))
    return blocks


def text_to_children(text: str):
    text_nodes = text_to_text_nodes(text)
    html_nodes = []

    for textnode in text_nodes:
        html_nodes.append(text_node_to_html_node(textnode))

    return html_nodes


def get_header_level(header: str) -> int:
    level = 0
    for character in header:
        if character == "#":
            level += 1
        else:
            break

    return level


def remove_md_marking(index: int, line: str) -> str:
    return line[index:].strip()


def render_list_as_html_nodes(block: str, list_type: str):
    index = 0
    if list_type == "ul":
        index = 1
    elif list_type == "ol":
        index = 2

    html_node_list = []
    ul_item_list = block.split("\n")
    for item in ul_item_list:
        clean = remove_md_marking(index, item)
        html_node_list.append(ParentNode("li", text_to_children(clean)))
    return ParentNode(list_type, html_node_list)


def render_code_as_html_node(block: str):
    htmlnodes = []
    htmlnodes.append(
        text_node_to_html_node(
            TextNode(block.replace("```\n", "").replace("```", ""), TextType.CODE)
        )
    )
    return ParentNode("pre", htmlnodes)


def render_blockquote_as_html_node(block: str):
    blockquote: list[str] = []
    for line in block.split("\n"):
        blockquote.append(remove_md_marking(1, line))

    return ParentNode("blockquote", text_to_children("\n".join(blockquote)))


def markdown_to_html_node(md: str):
    blocks = markdown_to_blocks(md)
    htmlnodes = []
    for block in blocks:
        match block_to_blocktype(block):
            case BlockType.PARAGRAPH:
                htmlnodes.append(
                    ParentNode("p", text_to_children(block.replace("\n", " ")))
                )

            case BlockType.HEADING:
                level = get_header_level(block)
                htmlnodes.append(
                    ParentNode(
                        f"h{level}",
                        text_to_children(remove_md_marking(level, block)),
                    )
                )

            case BlockType.QUOTE:
                htmlnodes.append(render_blockquote_as_html_node(block))

            case BlockType.UNORDERED_LIST:
                htmlnodes.append(render_list_as_html_nodes(block, "ul"))

            case BlockType.ORDERED_LIST:
                htmlnodes.append(render_list_as_html_nodes(block, "ol"))

            case BlockType.CODE:
                html_node = text_node_to_html_node(TextNode(block, TextType.CODE))
                htmlnodes.append(render_code_as_html_node(block))

    return ParentNode("div", htmlnodes)
