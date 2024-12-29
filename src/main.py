from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from inline_markdown import split_nodes_delimiter
from block_markdown import markdown_to_blocks
from copy_source_to_dest import copy_source_to_dest
def main():
    copy_source_to_dest("static","public")

main()