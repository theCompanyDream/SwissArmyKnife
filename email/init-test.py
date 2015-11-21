from constants import ENV

def createEmail(template, model):
    template = ENV.get_template(template)
    return template.render(model)

model = {
    "companyName": "Bullshit",
    "DateVisited": "something",
    "items": [{"name": "Yup"}],
    "myName": "It\'s Tim Nigga"}

print(createEmail('ThankYouLetter01.template', model));
