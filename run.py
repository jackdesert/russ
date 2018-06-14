# Print a list of stories from russianlife.com,
# plus a link to each story and a url for
# the title image

from bs4 import BeautifulSoup
import requests

base = 'https://russianlife.com'
html_doc = requests.get(base).text
soup = BeautifulSoup(html_doc, 'html.parser')
dates = soup.find_all('div', 'blog-date')

for date in dates:
    parent = date.parent

    image_tag = parent.find('div', 'blog-image')
    title_tag = parent.find('div', 'blog-title')

    image_path = image_tag.find('img').attrs['src']
    story_path = title_tag.find('a').attrs['href']

    title = title_tag.text

    print(f'\n\n{title}\n  {base}{story_path}\n  {base}{image_path}')
