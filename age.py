import requests

url = "http://www.facexapi.com/get_image_attr?"

payload = {'image_attr': ''}
files = [
    ('image', open('kimmich.jpg','rb'))
]
headers = {
  'user_id': '600f1d2f193a746f8f3eeb00',
  "Content-Type":"application/json"
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))


# import requests

# url = "https://search.facex.io:8443/images/singleImage/"

# payload = {'user_id': 'c884995e2ffdc8467558',
# 'name': 'Person\'s Name'}
# files = [
#   ('image', open('/path/to/file','rb'))
# ]
# headers= {}

# response = requests.request("POST", url, headers=headers, data = payload, files = files)

# print(response.text.encode('utf8'))