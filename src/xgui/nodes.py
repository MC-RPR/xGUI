import tkinter as tk

try:
    import defusedxml.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class AbstractNodeVisitor(object):
    def __init__(self, root: tk.Tk):
        self.root = root

    def visit(self, node: ET.Element):
        method = "visit_" + node.tag
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def tree_visit(self, node: ET.Element):
        for child in node:
            self.visit(child)

    def generic_visit(self, node: ET.Element):
        raise NotImplementedError(f"Tag <{node.tag}> is not implemented")

    def organize(self, item, node: ET.Element):
        raise NotImplementedError


class WidgetVisitor(AbstractNodeVisitor):
    def visit_Frame(self, node: ET.Element):
        res = tk.Frame(self.root)
        self.__class__(res).tree_visit(node)
        return self.organize(res, node)

    def visit_Button(self, node: ET.Element):
        return self.organize(tk.Button(self.root, text=node.text), node)

    def visit_Label(self, node: ET.Element):
        return self.organize(tk.Label(self.root, text=node.text), node)

    def visit_Entry(self, node: ET.Element):
        return self.organize(tk.Entry(self.root), node)

    def visit_Checkbutton(self, node: ET.Element):
        return self.organize(tk.Checkbutton(self.root, text=node.text), node)

    def visit_config(self, node: ET.Element):
        print("Ignoring config for now")


class PackVisitor(WidgetVisitor):
    def organize(self, item, node: ET.Element):
        return item.pack()
