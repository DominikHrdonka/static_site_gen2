from textnode import TextNode, TextType

def main():
    node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node1)

main()