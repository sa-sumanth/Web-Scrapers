import requests
import bs4

req = requests.get("https://in.linkedin.com/jobs/python-developer-jobs?position=1&pageNum=0")
soup = bs4.BeautifulSoup(req.text, "html.parser")

print(soup.title.text)

contents = dict()

for t in soup.findAll("div", "result-card__contents"):
        tle = t.find("h3", "result-card__title").text
        contents[tle] = []
        
        h = t.find("h4", "result-card__subtitle")
        contents[tle].append(h.text)
        r = t.find("div", "result-card__meta")
        contents[tle].append(r.text)

for i in contents:
        print(i)
        print("Company : {}\nLocation : {}".format(contents[i][0], contents[i][1]))
        print()