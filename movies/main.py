from bs4 import BeautifulSoup
import requests
import lxml
import re
# with open('website.html', 'r') as html_doc:
#     contents = html_doc.read()
# soup = BeautifulSoup(contents, 'html.parser')
# all_anchor_tags = soup.find_all(name='a')
# for anchor_tags in all_anchor_tags:
#     print(anchor_tags.string)
#     print(anchor_tags.get('href'))
# heading = soup.find(name='h3', class_='heading')
# print(heading.getText())
# company_url = soup.select_one(selector='p em')
# print(company_url)
#
# name = soup.select_one(selector='#name')
# print(name)
#
# headings = soup.select(selector='.heading')
# for heading in headings:
#     print(heading)
#
# response = requests.get(url="https://news.ycombinator.com/")
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
# article_tags = soup.find_all(name='a', class_ ='storylink')
#
# upvotes = soup.find_all(name='span', class_='score')
# article_titles = []
# article_links = []
# article_upvotes = [int(upvote.getText().split()[0]) for upvote in upvotes]
#
# # print(top_headlines)
# for article in article_tags:
#     article_titles.append(article.getText())
#     article_links.append(article.get('href'))
#
# top_score = max(article_upvotes)
# top_score_index = article_upvotes.index(top_score)
# print(article_titles[top_score_index])
# dct = {}
# print(article_titles)
#
# for index in range(len(article_upvotes)):
#     score = (str(article_upvotes[index]))
#     dct[score]={article_titles[index]: article_links[index]}
#
#
#
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')
top_movies = soup.find_all(name='h3', class_='title')
ascending_ranked_movies= [movie.getText() for movie in top_movies][::-1]
print(ascending_ranked_movies)
with open("top_movies.txt", 'w') as movie_rankings:
    for movie in ascending_ranked_movies:
        movie_rankings.write(f"{movie}\n")


