import requests
from io import BytesIO

# Replace with your Imgur client ID
client_id = 'bb7dd5ec669962a'
headers = {'Authorization': f'Client-ID {client_id}'}

# Replace with your image data (e.g., from a URL or other source)
image_data = b'GUI/pimage_2.png'  # Replace with actual image data as bytes

# Create a BytesIO object from the image data
image_file = BytesIO(image_data)

# Upload the image
response = requests.post(
    'https://api.imgur.com/3/image',
    headers=headers,
    files={'image': image_file}
)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Extract and print the URL of the uploaded image
    image_url = response_data['data']['link']
    print(f'Image URL: {image_url}')
else:
    # Print the error message
    print(f'Failed to upload image. Status code: {response.status_code}')
    print(response.json())
