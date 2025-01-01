from copy_source_to_dest import copy_source_to_dest
from page_generator import generate_pages_recursive
import os
def main():
    copy_source_to_dest("static","public")
    generate_pages_recursive("content","template.html","public")
main()