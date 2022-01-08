from .utils import DummyClass, dummy_function, requires_module

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    Environment, FileSystemLoader = DummyClass()
    select_autoescape = dummy_function


class Jinja2(object):
    def __init__(self, template_path: str):
        self.env = Environment(
            loader=FileSystemLoader(template_path),
            autoescape=select_autoescape()
        )

    @requires_module("jinja2")
    def render(self, s: str):
        return self.env.from_string(s).render()
