import os
from markdownify import markdownify as md

# Options
SOURCE = "bibliography.html"
DEST = "bibliography.md"
DELETE_SOURCE_FILE = True

# Set yaml header with post metadata
header = """---
layout: page
title: "Bibliography"
---
"""


if __name__ == '__main__':
    with open(SOURCE ) as f:
        data = f.read()

# Convert html to markdown
mdwn = md(data)

# Add header and # to title
txt = header + "# " + mdwn.lstrip()

with open(DEST, "w") as f:
    f.write(txt)
    
if DELETE_SOURCE_FILE:
   os.remove(SOURCE) 