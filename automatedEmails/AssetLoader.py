from jinja2 import BaseLoader, TemplateNotFound
from os.path import join, exists, getmtime

class AssetLoader(BaseLoader):
    def __init__(self, path):
        self.path = path

    def get_source(self, enviorment, templates):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
        mtime = getmtime(path)
        with file(path) as f:
            source = f.read().decode('utf-8')
        return source, path, lambada: mtime == getmtime(path)
