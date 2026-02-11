from textnode import TextNode, TextType
import re


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for text_node in old_nodes:
        if text_node.text_type != TextType.TEXT:
            new_nodes.append(text_node)
            continue

        split_nodes = []

        fragments = text_node.text.split(delimiter)
        if len(fragments) % 2 == 0:
            raise ValueError(f"Invalid combination of delimiter: {delimiter}")

        for i in range(len(fragments)):
            if fragments[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(fragments[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(fragments[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\]]+)\]\(([^\)]+)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\]]+)\]\(([^\)]+)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]):
    results = []
    for node in old_nodes:
        links = extract_markdown_images(node.text)
        if len(links) == 0:
            results.append(node)
            continue

        current_text = node.text
        for link in links:
            link_str = f"![{link[0]}]({link[1]})"
            items = current_text.split(link_str, maxsplit=1)

            before = items[0]
            if before:
                results.append(TextNode(before, TextType.TEXT, None))
            results.append(TextNode(link[0], TextType.IMAGE, link[1]))
            current_text = items[1]
        if current_text:
            results.append(TextNode(current_text, TextType.TEXT, None))

    return results


def split_nodes_link(old_nodes: list[TextNode]):
    results = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            results.append(node)
            continue

        current_text = node.text
        for link in links:
            link_str = f"[{link[0]}]({link[1]})"
            items = current_text.split(link_str, maxsplit=1)

            before = items[0]
            if before:
                results.append(TextNode(before, TextType.TEXT, None))
            results.append(TextNode(link[0], TextType.LINK, link[1]))
            current_text = items[1]
        if current_text:
            results.append(TextNode(current_text, TextType.TEXT, None))

    return results


def text_to_text_nodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    results = split_nodes_delimiter([initial_node], "**", TextType.BOLD)
    results = split_nodes_delimiter(results, "_", TextType.ITALIC)
    results = split_nodes_delimiter(results, "`", TextType.CODE)
    results = split_nodes_link(results)
    results = split_nodes_image(results)
    return results
