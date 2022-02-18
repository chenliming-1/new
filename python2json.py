# -*- coding:utf-8 -*-
import json


def Python_to_json():
    """Python对象转换为json"""
    d={
        'name':'python书籍',
        'price':'62.3',
        'is_valid':True
    }
    res = json.dumps(d,ensure_ascii=False,indent=2)
    print(res)
def json_to_python():
    """json对象转换为python"""
    data="""{
    "success":true,
    "errorCode":null,
    "message":"获取成功",
    "currentTime":"2022-02-18T17:03:54.482+0800",
    "data":"teacher-tr-rls.entstudy.com"
    }"""
    res2=json.loads(data)
    print(res2)
    print(res2["success"])

def jsonFile_to_python():
    """从文件读取内容，转换为python
        data数据为从json文件中读取的数据，但是格式仍然为json格式，
        所以要使用json.load()方法转换数据格式后才可以在python 当中获取
    """
    f = open('.\data.json','r',encoding="utf-8")
    data = f.read()
    data1=json.loads(data)
    print(data1["success"])
    f.close()
if __name__ == '__main__':
    Python_to_json()
    json_to_python()
    # jsonFile_to_python()
