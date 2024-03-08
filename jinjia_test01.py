from jinja2 import Template

template  = Template("THis is test file output: {{output}} ")

result = template.render(output=' jinja test file 01 output')

print(result)