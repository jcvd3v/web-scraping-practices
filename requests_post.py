import requests
data = {'name':'J', 
        'mesage':'Hello world!'}
url = 'https://httpbin.org/post'
r= requests.post(url, json=data)

response_data = r.json()
print(response_data)