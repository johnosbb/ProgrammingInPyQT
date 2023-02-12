import re
method = 'images/:id/huge'
result = re.sub(r'(:[a-z]+)', r'<span>\1</span>', method)
print(result)

html = "font-family:'Verdana','Other'; font-weight:456; font-style:italic;"
result = re.sub(r"(font-family:)('.+'),('.+')", r'\1\3', html)
print(result)
