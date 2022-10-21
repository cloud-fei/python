#引入第三方模块
import json


#python dict
python_dict = {
'name' : 'myname',
'age' : 100,
}
print("python dict = ",python_dict)   # python dict =  {'name': 'myname', 'age': 100}


#python dict to json string
json_str = json.dumps(python_dict)
print("json string = ",json_str)     # json string =  {"name": "myname", "age": 100}

#json string to python dict
re_python_dict = json.loads(json_str)
print("re python dict = ",re_python_dict)  # re python dict =  {'name': 'myname', 'age': 100}


#想要添加字段时，使用python dict 的 update 方法来实现
height = {'height': 180}
python_dict.update(height)
print("new python dict = ",python_dict)   # new python dict =  {'name': 'myname', 'age': 100, 'height': 180}

#json.dump() 和 json.load() 用于处理文件
with open('test.json', 'r') as f:
    json.load(f)                         # read file, json string to python dict 

data = python_dict
with open('test.json', 'w') as f:
    json.dump(data, f)                   # python dict to json string, write file


