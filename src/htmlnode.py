
class HTMLNode():
    def __innit__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(list(map(lambda prop: f' {prop}="{self.props[prop]}"',self.props)))
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"