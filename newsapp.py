import requests
import json

query=input("What news you are intrestred: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-06-09&sortBy=publishedAt&apiKey=3ec9e6c943cb4430b7b2d18705af0214"
r=requests.get(url)
news = json.loads(r.text)
# print(news)
for articles in news["articles"]:
    print(articles["title"])
    print(articles["description"])
    print("______________________________________________")