from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
# print(response.text)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
# article_tag = soup.find(name='a', class_='a')
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()

# print(article_text)
# print(article_link)
# print(article_upvote)
articles = []
for div in soup.findAll('td'):
    if div.attrs=={'class': ['title']}:
        anchor = div.find('a')
        anchor_link = anchor.get('href')
        anchor_text = anchor.getText()
        print(f'{anchor_text} | {anchor_link}')
    if div.attrs=={'class': ['subtext']}:
        span = div.find('span', class_='score')
        if span != None:
            upvote = span.getText()
            print(f'{upvote}')
#     if div.find('a') != None :
#         print(div.find('a')['href'])
#     if div.find('span') != None:
#         print(div.find('span', class_='score'))

# for div in soup.findAll('td', attrs={'class':'subtext'}):
#     print(div.find('span', class_='score'))





# with open('website.html') as file:
#     content = file.read()

# # print(content)
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.title)

# # print(soup.prettify())
# # print(soup.p)

# all_anchor_tags = soup.find_all(name = 'a')

# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get('href'))

# # heading=soup.find(name='h1')
# # heading=soup.find(name='h1', id='name')
# # section_heading=soup.find(name='h3', class_='heading')
# # print(section_heading)

# # company_url = soup.select_one(selector='p a')
# # print(company_url)

# headings = soup.select('.heading')
# print(headings)