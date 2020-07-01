from requests import get
from bs4 import BeautifulSoup as BS
import json

username = 'fitmomblogger'

resp = get(f'https://instagram.com/{username}')
soup = BS(resp.text, 'html.parser')
scripts = soup.find_all('script')
data_script = scripts[4]

content = data_script.contents[0]
data_object = content[content.find('{"config"'): -1]
data_json = json.loads(data_object)
data_json = data_json['entry_data']['ProfilePage'][0]['graphql']['user']

result = {
    'bio': data_json['biography'],
    'external_url': data_json['external_url'],
    'followers_count': data_json['edge_followed_by']['count'],
    'following_count': data_json['edge_follow']['count'],
    'full_name': data_json['full_name'],
    'is_private': data_json['is_private'],
    'is_verified': data_json['is_verified'],
    'username': data_json['username'],
    'posts_count': data_json['edge_owner_to_timeline_media']['count']
}
print(result)
