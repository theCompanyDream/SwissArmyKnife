from jinja2 import Environment, PackageLoader
from AssetLoader as loader

class Templates:
    def __init__(self, loader):
        self.env = Environment(loader=loader)

    def gen_Email(templateName, object):
        assert type(templateName) is StringType, "Value entered is not a string"
