import json
import pytest
from qdecrypt import *


@pytest.fixture(scope="module", autouse=True)
def my_qtree():
    return QTree(ref_file="tests/reference_files/qdecrypt.csv")


def test_ref_file(my_qtree):
    assert my_qtree.ref_file == "tests/reference_files/qdecrypt.csv"


def test_create_tree(my_qtree):
    tree = my_qtree._create_tree("qQa")
    assert tree.depth() == 3
    d = tree.to_dict()
    assert d == {
        "QQA": {
            "children": [
                {
                    "Q: TTS": {
                        "children": [
                            {
                                "QQ: Office of Solutions": {
                                    "children": ["QQA: Data & Analytics"]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
