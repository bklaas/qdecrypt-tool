import csv
from collections import defaultdict
import sys

from treelib import Node, Tree

decrypt = defaultdict(lambda: "???")
with open("qdecrypt.csv", "r") as csvf:
    r = csv.DictReader(csvf)
    for row in r:
        decrypt[row['stub']] = row['desc']

acronym = sys.argv[1].upper()

if not acronym.startswith("Q"):
    raise KeyError("acronym must start with Q")

qtree = Tree()
qtree.create_node(acronym, 1)
for idx, x in enumerate(acronym, start=1):
    node = idx + 1
    substr = acronym[0:idx]
    qtree.create_node(f"{substr}: {decrypt[substr]}", node, parent=idx)
qtree.show()