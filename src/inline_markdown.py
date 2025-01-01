from textnode import TextType,TextNode
import re

def extract_markdown_images(text):
    #![alt text for image](url/of/image.jpg)
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    urls_and_alt_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return urls_and_alt_text
def extract_markdown_links(text):
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    links_and_anchor_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return links_and_anchor_text


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

def split_nodes_image(old_nodes):
    #"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text:
            continue
        remaining_text = old_node.text
        extracted_images = extract_markdown_images(remaining_text)
        if not extracted_images:
            new_nodes.append(old_node)
            continue
        for extracted_image in extracted_images:
            image_alt = extracted_image[0]
            image_link = extracted_image[1]
            sections = remaining_text.split(f"![{image_alt}]({image_link})",1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
                
            new_nodes.append(TextNode(image_alt,TextType.IMAGE,image_link))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes
        
            
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text:
            continue
        remaining_text = old_node.text
        extracted_links = extract_markdown_links(remaining_text)
        if not extracted_links:
            new_nodes.append(old_node)
            continue
        for extracted_link in extracted_links:
            link_text = extracted_link[0]
            link = extracted_link[1]
            sections = remaining_text.split(f"[{link_text}]({link})",1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0]:
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
                
            new_nodes.append(TextNode(link_text,TextType.LINK,link))
            remaining_text = sections[1]
            
        if remaining_text:
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text,TextType.TEXT)
    node_code = split_nodes_delimiter([text_node],"`",TextType.CODE)
    node_bold = split_nodes_delimiter(node_code,"**",TextType.BOLD)
    node_italic = split_nodes_delimiter(node_bold,"*",TextType.ITALIC)
    node_images = split_nodes_image(node_italic)
    node_link = split_nodes_link(node_images)
    return node_link
    