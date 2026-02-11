class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"tag: {self.tag} \nvalue: {self.value} \nchildren: {self.children} \nprops: {self.props}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("No value in leafnode.")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)
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
