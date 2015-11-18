from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('Email','templates'))
template = env.get_template('thankyouNote.template')
print(template.render(name='Tim Brantley II'))