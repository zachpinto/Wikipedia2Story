import requests
import re


def fetch_wikipedia_content(page_title):
    # Encode the page title to handle spaces and special characters
    url_title = requests.utils.quote(page_title)

    # Request URL for the Wikipedia API
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&format=json&titles={url_title}"

    # Make the API request
    response = requests.get(url)
    response.raise_for_status()

    # Extract the page content
    data = response.json()
    page = next(iter(data['query']['pages'].values()))

    if 'extract' in page:
        content = page['extract']
        # Remove sections like 'See also', 'References', etc. We don't need them.
        content = re.sub(r'==\s*(See also|Notes|References|Further reading|External links)\s*==.*', '', content,
                         flags=re.S)
        return content.strip()
    else:
        return "No content available for this page."


# Function to fetch the content of a Wikipedia page
# The function takes the page title as input and returns the content of the page
# This will be passed into the main function in the streamlit app
def main(page_title):
    content = fetch_wikipedia_content(page_title)
    return content
