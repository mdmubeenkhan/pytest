import requests

def user_list():
    print("user list entry")
    response = requests.get("http://localhost:8000/user/")
    if response.status_code ==200:
        return response
    else:
        return {"data":"failed to get user details."}


def get_len():
    print("get len entry")
    data = user_list()
    print(data, "get len exit")
    return data

# get_len()
# print(response.text)
# print(response.status_code)
# print(response.json())