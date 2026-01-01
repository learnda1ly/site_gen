from textnode import TextNode, TextType


def main():
    test_text_node = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev")
    print(test_text_node)


main()
