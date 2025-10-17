import json

#Python to json
#dump(obj, file) : writes JSON to file
data = {
    "id" : "DATA£2223",
    "tasks" : [{"id" : 12213, "name" : "task1"}, {"id" : 12213, "name" : "task1"},
               {"id" : 12213, "name" : "task1"},
               {"id" : 12213, "name" : "task1"}]
}

with open("./CLASS 11/tasks.json", "w") as f:
    json.dump(data, f, indent=2)


#dumps : returns a JSON STRING
text = json.dumps(data)


#json.load(file_obj) : reads JSON from a file
with open("./CLASS 11/students.json") as f:
    data = json.load(f)

print(data)

#json.loads(text) : parses a JSON string
parsed = json.loads(text)
print(type(parsed))