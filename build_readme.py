#! /usr/bin/env python3

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

# Save
with open("README.rst", "w") as f:
    f.write("\n\n".join(blocks))