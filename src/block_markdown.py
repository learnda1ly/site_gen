def markdown_to_blocks(markdown: str):
    results = []
    for line in markdown.split("\n\n"):
        results.append(line.strip("\n"))
    return results
