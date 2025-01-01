from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,TextType,text_node_to_html_node
from inline_markdown import text_to_textnodes
def markdown_to_blocks(markdown):
    block_strings_list = []
    markdown_document_split = markdown.split("\n\n")
    for block in markdown_document_split:
        if block == "" or block == "\n":
            continue
        block_strings_list.append(block.strip())
    return block_strings_list


def block_to_block_type(block):
    heading_tuple = ("######", "#####", "####", "###", "##", "#")
    if block.startswith(heading_tuple):
        return "heading"
    
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    
    elif block.startswith(">"):
        block_lines = block.splitlines()
        for line in block_lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
        
    elif block.startswith("* ") or block.startswith("- "):
        block_lines = block.splitlines()
        for line in block_lines:
            if not line.startswith("* ") and not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    elif block[0] == "1":
        block_lines = block.splitlines()
        current_number = 1
        for line in block_lines:
            ol_number = line.split()[0]
            if ol_number != f"{current_number}.": 
                return "paragraph1"
            current_number += 1
        return "ordered_list"
    
    else:
        return "paragraph"

def text_to_children(text):
    child_text_nodes = text_to_textnodes(text)
    child_leaf_nodes = []
    for text_node in child_text_nodes:
        child_leaf_node = text_node_to_html_node(text_node)
        child_leaf_nodes.append(child_leaf_node)
    return child_leaf_nodes

def block_to_HTML_Node(block):
    block_type = block_to_block_type(block)
    if block_type == "heading":
        block_text = block.lstrip("#")
        if block.startswith("######"):
            return ParentNode("h6",text_to_children(block_text))
        elif block.startswith("#####"):
            return ParentNode("h5",text_to_children(block_text))
        elif block.startswith("####"):
            return ParentNode("h4",text_to_children(block_text))
        elif block.startswith("###"):
            return ParentNode("h3",text_to_children(block_text))
        elif block.startswith("##"):
            return ParentNode("h2",text_to_children(block_text))
        elif block.startswith("#"):
            return ParentNode("h1",text_to_children(block_text))
    elif block_type == "quote":
        block_text = []
        block_lines = block.splitlines(keepends=True)
        for text in block_lines:
            text = text.lstrip(">")
            block_text.append(text)
        block_text = "\n".join(block_text)
        return ParentNode("blockquote",text_to_children(block_text))
    elif block_type == "unordered_list":
        list_items_nodes = []
        split_list = block.splitlines(keepends=True)
        for list_item in split_list:
            list_item = list_item.lstrip("*").lstrip("-")
            list_item_node = text_to_children(list_item)
            list_items_nodes.append(ParentNode("li",list_item_node))
        return ParentNode("ul",list_items_nodes)
    elif block_type == "ordered_list":
        list_items_nodes = []
        split_list = block.splitlines(keepends=True)
        for list_item in split_list:
            list_item = list_item.lstrip("0123456789. ")
            list_item_node = text_to_children(list_item)
            list_items_nodes.append(ParentNode("li",list_item_node))
        return ParentNode("ol",list_items_nodes)
    elif block_type == "code":
        block_text = block.replace("```","")
        return ParentNode("pre",[ParentNode("code",text_to_children(block_text))])
    else: 
        return ParentNode("p",text_to_children(block))
          

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for markdown_block in markdown_blocks:
        html_node = block_to_HTML_Node(markdown_block)
        html_nodes.append(html_node)
    return ParentNode("div",html_nodes)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("#"):
            block = block.lstrip("#")
            block = block.strip()
            return block
    raise Exception("Missing h1 header!")