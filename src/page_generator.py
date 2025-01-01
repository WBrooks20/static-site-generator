from block_markdown import markdown_to_html_node,extract_title
from copy_source_to_dest import copy_source_to_dest
import os
def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path,"r")
    from_contents = f.read()
    t = open(template_path,"r")
    template_contents = t.read()
    html_string = markdown_to_html_node(from_contents).to_html()
    html_title = extract_title(from_contents)
    html_page = template_contents.replace("{{ Title }}",html_title)
    html_page = html_page.replace("{{ Content }}",html_string)
    write_file = open(dest_path,"w")
    write_file.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for directory_path,dir,files in os.walk(dir_path_content):
        for file in files: 
            #source full file path
            file_path = os.path.join(directory_path,file)
            #source path to file without the root (ex: content/majesty/index.md is majesty)
            rel_path = directory_path.split("/")
            rel_path = rel_path[1:]
            rel_path = "/".join(rel_path)
            #relative path without the root and the file (ex content/majesty/index.md is majesty/index.md)
            if not rel_path:
                dest_path = dest_dir_path
            else: 
                dest_path = f"{dest_dir_path}/{rel_path}"
            if ".md" in file:
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                file_name = file.replace(".md",".html")
                generate_page(file_path,template_path,f"{dest_path}/{file_name}")

                    