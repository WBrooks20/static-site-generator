import os
import shutil
def copy_source_to_dest(source,destination,path=""):
    current_source_path = f"{path}{source}"
    current_dest_path = f"{destination}/{current_source_path}".replace("/static","")
    print (f"Loop dest: {current_dest_path}")
    if os.path.exists(f"{current_dest_path}"):
        print(f"Removing existing path: {current_dest_path}")
        shutil.rmtree(f"{current_dest_path}")
    

    if not os.path.exists(f"{destination}/{current_source_path}"):
        print(f"Creating destination path {current_dest_path}")
        os.mkdir(current_dest_path)
    
    print(f"Current source path: {current_source_path}")
    directory_contents = os.listdir(current_source_path)

    
    for directory_item in directory_contents:
        src_item_path = f"{current_source_path}/{directory_item}"
        dest_item_path = f"{destination}/{current_source_path}/{directory_item}".replace("static/","")
        print (f"Source item path: {src_item_path} \n dest item path: {dest_item_path}")
        if os.path.isdir(src_item_path):
            print("-------------------------------------------------")
            print(f"source: {directory_item}\ndestination: {destination}\npath: {current_source_path}/")
            copy_source_to_dest(directory_item,f"{destination}",f"{current_source_path}/")

        elif os.path.isfile(src_item_path):
            print (f"Copying item: {directory_item} to dest path {dest_item_path}")
            shutil.copy(src_item_path,dest_item_path)
        
            