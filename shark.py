import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://example.com'

# Send a GET request to the URL and retrieve the page content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and extract specific elements from the parsed HTML
    # For example, let's extract all the links on the page
    links = soup.find_all('a')

    # Print the extracted links
    for link in links:
        print(link.get('href'))
else:
    print('Failed to retrieve the webpage')
