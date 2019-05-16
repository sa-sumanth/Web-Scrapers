import requests
import bs4

req = requests.get("https://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012")
soup = bs4.BeautifulSoup(req.text, "html.parser")
print(soup.title.text + "\n\n")
contents = dict()

for h in soup.findAll("div","lister-item-content")[:10]:
        movie = h.find("h3", "lister-item-header").text
        contents[movie] = []
        e = h.findAll("p")
        contents[movie].append(e[0].find("span", "runtime").text)
        contents[movie].append(e[0].find("span", "genre").text)
        contents[movie].append(e[1].text)
        contents[movie].append(h.find("strong").text)
        crew = []
        for i in e[2].findAll("a"):
                crew.append(i.text)
        contents[movie].append(crew)

for i in contents:
        title = i.split("\n")
        print(" ".join(c for c in title[1:]))
        print("Genre : " + contents[i][1].strip() + "\t" + "Runtime : " + contents[i][0])
        print("Movie summary : " + contents[i][2].strip())
        print("IMDb Rating : " + contents[i][3] + "/10")
        print("Director : " + contents[i][4][0])
        print("Stars : " + ", ".join(c for c in contents[i][4][1:]))
        print("\n")