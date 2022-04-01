from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
story_link = soup.find_all(name='a', attrs={'class': 'titlelink'})
story_link_text = [link.text for link in story_link]
story_link_href = [link.get('href') for link in story_link]
article_points = [score.text for score in soup.find_all(name='span', attrs={'class': 'score'})]
points = [int(point.replace(' points', '')) for point in article_points]


def get_highest_points(points):
    highest_points = max(points)
    return points.index(highest_points)



# print(get_highest_points(points))
print(story_link_text[get_highest_points(points)],"\n",story_link_href[get_highest_points(points)])


# print(story_link_href)
# print(points)
# print(story_link)




# with open("website.html", "r") as f:
#     contents = BeautifulSoup(f.read(), "html.parser")
#
# # print(contents.prettify())
# all_headings = contents.find_all("p").__getitem__().text
# print((all_headings))



