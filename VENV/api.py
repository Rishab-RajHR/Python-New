import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print("Status: ",response.status_code)
# print("Data: ",response.json())

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Alex Pandian",
    "body": "This is the post created by Alex.",
    "userId": 1
}

response = requests.post(url, json=new_post)
print("Status: ", response.status_code)
print("Data: ", response.json())