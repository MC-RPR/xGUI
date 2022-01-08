import tkinter as tk

try:
    import defusedxml.ElementTree as ET

    _defused_xml = True
except ImportError:
    import xml.etree.ElementTree as ET

    _defused_xml = False

from .nodes import PackVisitor


def load(filename: str, root=None):
    if root is None:
        root = tk.Tk()

    if _defused_xml:
        tree = ET.parse(filename, forbid_dtd=True)
    else:
        tree = ET.parse(filename)

    PackVisitor(root).tree_visit(tree.getroot())

    return root


def load_string(xml_string: str, root=None):
    if root is None:
        root = tk.Tk()

    tree = ET.fromstring(xml_string)
    PackVisitor(root).tree_visit(tree.getroot())

    return root
