#jsons
import json
"""
need ot be fixed
data =  '{  "firstName": "Jane",
            "lastName": "Doe",
            "hobbies": ["running", "sky diving", "singing"],
            "age": 35,
            "children": [
                        {
                            "firstName": "Alice",
                            "age": 6
                        },
                        {
                            "firstName": "Bob",
                            "age": 8
                        }
                        ]
        }'
"""

data = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
json_acceptable_string = data.replace("'", "\"")
d = json.loads(json_acceptable_string)
print(type(d))
# d = {u'muffin': u'lolz', u'foo': u'kitty'}
# d = <class 'dict'>
