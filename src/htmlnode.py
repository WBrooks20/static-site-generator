
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props is None:
            return ""
        return str("".join(list(map(lambda prop: f' {prop}="{self.props[prop]}"',self.props))))
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        
    def to_html(self):
        if not self.value:
            raise ValueError ("LeafNode has no value.")
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    #constructor. Inherit parent constructor where value=none because parent nodes do not have a value.
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)
        #To html method for parent nodes. 
    def to_html(self):
        #parent nodes must have tags and children.
        if not self.tag:
            raise ValueError ("missing tag!")
        if not self.children:
            raise ValueError("Missing Children!")
        #Create the string. Each recursive call to the function(parent nodes) will create its own html_string with the tag of the parent node. 
        html_string = f"<{self.tag}{self.props_to_html()}>"
        #iterate over children of current parent node. 
        for child in self.children:
            #if the child of the parent node is itself a parent node we need to recursively call to_html()(the parent node method) to create its own html string, recursively append the to_html method results of its child nodes to its html string, and return its html_string to be appended to the previous calls html string. 
            #if the child of the parent node is a leaf node then it calls to_html(the leaf node method) to format the leafnodes data and appends that to the html_string of the current function call. 
            html_string += child.to_html().strip()
        html_string += f"</{self.tag}>"
        return html_string
    def __repr__(self):
       return f"ParentNode({self.tag}, {self.children}, {self.props})" 
        
        
    