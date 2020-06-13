import json
with open("README.md") as f:
    lines = f.read()
with open("config.json") as a:
    jsson = a.read()
    jsson = json.loads(jsson)


print(lines.replace(jsson["templating"], "lol"))