from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(
            self,
            tag: str,
            children: list[HTMLNode],
            props: dict[str: str] | None = None
    ) -> None:
        super()
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode does not have a tag")
        if self.children is None:
            raise ValueError("ParentNode has no children")

        html = ""

        for child in self.children:
            html += child.to_html()

        return f"<{self.tag}>{html}</{self.tag}>"
