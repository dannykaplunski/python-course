import yaml
document = """
  a: 1
  b:
    c: 3
    d: 4
"""
loaded = yaml.load(document, Loader=yaml.FullLoader)
print(loaded)
loaded['a'] = 2
dumped = yaml.dump(loaded)
print(dumped)