from jinja2 import FileSystemLoader, Environment

ENV = Environment(loader = FileSystemLoader(searchpath ='./assets', encoding='utf-8', followlinks=True))
