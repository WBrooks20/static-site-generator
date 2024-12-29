def markdown_to_blocks(markdown):
    block_strings_list = []
    markdown_document_split = markdown.split("\n\n")
    for block in markdown_document_split:
        if block == "":
            continue
        block_strings_list.append(block.strip())
    return block_strings_list