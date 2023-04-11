import requests
from bs4 import BeautifulSoup

def parseNews(request):

    phrases = request.split(",")
    objects = []

    for phrase in phrases:
        phrase = phrase.strip()
        url = f"https://news.google.com/search?q={phrase}%20when%3A1y&hl=nl&gl=NL&ceid=NL%3Anl"
        response = requests.get(url)
        googleURL = "https://news.google.com/"
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")
        counter = 0
        for article in articles:
            headline = article.find("h3").get_text()
            link = article.find("a")["href"]
            response = requests.get(googleURL+link)
            result = {
                    "phrase": phrase,
                    "text": headline,
                    "link": response.url
                    }
            objects.append(result)
            counter += 1
            if counter > 10:
                break
    return objects