import requests

# URL the API públic
url = "https://jsonplaceholder.typicode.com/posts"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (code 200)
if response.status_code == 200:
    # Convert the response to JSON format (dictionary list)
    posts = response.json()
    
    # Print the titles of the first 5 posts
    print("\n")
    print("\n")
    print("------------------------------------------")
    for post in posts[:5]:
        print(f"ID: {post['id']} - Título: {post['title']}")
        print(f"------------------------------------------")
else:
    print("Error al conectar con la API")

print("\n")
