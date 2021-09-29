import csv
from collections import defaultdict
import sys

from treelib import Node, Tree


class QTree(object):
    def __init__(self, ref_file):
        self.ref_file = ref_file
        self.qexpand = defaultdict(lambda: "???")
        with open(self.ref_file, "r") as csvf:
            r = csv.DictReader(csvf)
            for row in r:
                self.qexpand[row["stub"]] = row["desc"]

    def _create_tree(self, acronym):
        acronym = acronym.upper()
        if not acronym.startswith("Q"):
            raise KeyError("acronym must start with Q")

        qtree = Tree()
        qtree.create_node(acronym, 1)
        for idx, x in enumerate(acronym, start=1):
            substr = acronym[0:idx]
            qtree.create_node(f"{substr}: {self.qexpand[substr]}", idx + 1, parent=idx)
        return qtree

    def show_tree(self, acronym):
        """display a full tree of information about a TTS Org acronym.

        Args:
            acronym (string): a TTS org chart acronym to expand

        Raises:
            KeyError: if string doesn't start with a Q or q

        Returns:
            treelib.Tree (object): the treelib.Tree object that describes the acronym
        """
        self._create_tree(acronym).show()


def main(acronym, ref_file="qexpand.csv"):
    qtree = QTree(ref_file)
    qtree.show_tree(acronym)


if __name__ == "__main__":
    try:
        acronym = sys.argv[1].upper()
    except IndexError:
        acronym = "QUEAAD"

    sys.exit(main(acronym))
