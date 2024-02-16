import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

query = "XYZ"
url = f'https://www.reddit.com/search/?q={query}'
page = requests.get(url)#, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

search_params = {
    'source': 'search',
    'action': 'view',
    'noun': 'post',
    'data-testid': 'search-post'
}
faceplate_list = soup.findAll(name="faceplate-tracker", attrs=search_params)

print(f'No. of posts extracted were {len(faceplate_list)}')
print()

for faceplate in faceplate_list:
    each_post_attr = faceplate.get('data-faceplate-tracking-context')

    # load json
    each_post_data = json.loads(each_post_attr)

    post_data = each_post_data.get('post', {})
    title = post_data.get('title', '')
    date_timestamp = post_data.get('created_timestamp', '')
    date = datetime.utcfromtimestamp(date_timestamp/1000.0).strftime('%Y-%m-%d %H:%M:%S')
    score = post_data.get('score', 0)
    subreddit_name = post_data.get('subreddit_name', '')
    number_comments = post_data.get('number_comments', 0)

    print(80*'#')
    # Print the attributes
    print("Title:", title)
    print("Date:", date)
    print("Score:", score)
    print("Subreddit Name:", subreddit_name)
    print("Number of Comments:", number_comments)
    print(80*'#')
    print()