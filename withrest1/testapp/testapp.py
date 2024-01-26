import json

import requests
A = 'http://127.0.0.1:8000/'
B = 'rest1/'

# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {
#             'id':id
#         }
#     resp=requests.get(A+B,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_data()

# def post_data():
#     new_data = {
#         'name':"rasi",
#         'rollno' : 4343,
#         'address' : 'america'
#     }
#     resp = requests.post(A+B,data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
# post_data()


# def put_data(id):
#     new_data={
#         'id':id,
#         'name': 'ramesh',
#         'rollno': 7654,
#     }
#     resp = requests.put(A+B,data = json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
# put_data(1)

def delete_data(id):
    delete_data={
        'id':id,
    }
    resp = requests.delete(A+B,data = json.dumps(delete_data))
    print(resp.status_code)
    print(resp.json())
delete_data(1)

