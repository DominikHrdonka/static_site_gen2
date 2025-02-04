class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        final_string = ""
        if self.props is not None:
            for key in self.props:
                final_string += " " + key + '="' + self.props[key] + '"'
        return final_string
    
    ###eq method not really needed for unittests, if we want to test props_to_html methods - Python knows how to compare strings
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def __repr__(self):
        return f"HTMLNode ({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        elif not self.tag:
            return self.value
        
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("Tag is required.")
        elif not isinstance(children, list):
            raise ValueError("Children must be a list.")
        elif len(children)==0:
            raise ValueError("Children cannot be empty.")
        
        for child in children:
            if not isinstance(child, HTMLNode):
                raise ValueError("Children must be an HTMLNode descendant")
        
        super().__init__(tag, children=children, props=props)
        
        