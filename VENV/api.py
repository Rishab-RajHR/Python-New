import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print("Status: ",response.status_code)
# print("Data: ",response.json())


# POST API

# url = "https://jsonplaceholder.typicode.com/posts"

# new_post = {
#     "title": "Alex Pandian",
#     "body": "This is the post created by Alex.",
#     "userId": 1
# }

# response = requests.post(url, json=new_post)
# print("Status: ", response.status_code)
# print("Data: ", response.json())

# PUT => Full data update

# url = "https://jsonplaceholder.typicode.com/posts/1"

# new_data = {
#     "title": "Updated Title",
#     "body": "This is the updated body of the post.",
#     "userId": 1
# }

# response = requests.put(url, json=new_data)

# print("Status: ", response.status_code)
# print("Data: ", response.json())


# Patch => Partial data update

# url = "https://jsonplaceholder.typicode.com/posts/1"

# new_data = {
#    "title": "Updated Title Two"
# }

# response = requests.patch(url, json=new_data)

# print("Status: ", response.status_code)
# print("Data: ", response.json())


# Delete => Remove the Field

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status: ", response.status_code)
if response.status_code == 200:
   print("Post deleted successfully.")
else:
   print("Failed to delete the post.")




