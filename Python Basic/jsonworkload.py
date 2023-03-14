import json

x = '{ "name" : "Duy", "age": 19}'
y = json.loads(x)
print(y, y["name"])

z = { "name" : "Duy", "age": 19}
p = json.dumps(z, indent=4)
# , separators=(". ", " = "))
print(p)
