#! /usr/bin/env python3

import os
import re

# Transfer sphinx contents
blocks = []
files = ["installing.rst", "overview.rst", "changelog.rst"]
with open("docs/source/index.rst") as f:
    block = f.read()
block = block.split("Table of Contents")[0]
blocks.append(block)
for file_name in files:
    with open("docs/source/%s" % file_name) as f:
        blocks.append(f.read())
blocks = [re.sub(r":py:(.+?):\`~*\.(.+?)\`", r"``\2``", block) for block in blocks]

# Is there an existing README to extract stuff from first?
if "README.rst" in os.listdir("."):
    with open("README.rst") as f:
        readme = f.read()
    match = re.search(r"\|.+\|(.|\n|\r)+?\n\n[^\.]", readme, re.MULTILINE)
    if match:
        lines = blocks[0].splitlines()
        lines.insert(2, "\n" + match[0][:-1].strip())
        blocks[0] = "\n".join(lines)

# Save
with open("README.rst", "w") as f:
    f.write("\n\n".join(blocks))