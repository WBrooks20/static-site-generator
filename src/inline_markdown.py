from textnode import TextType,TextNode
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text.count(delimiter) % 2 != 0:
          raise Exception ("Invalid markdown syntax. Missing closing or opening delimiter.")  
    
        split_text = old_node.text.split(delimiter)
        for i in range(0,len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i],TextType.TEXT))
            else: 
                new_nodes.append(TextNode(split_text[i],text_type))
                
    return new_nodes
        