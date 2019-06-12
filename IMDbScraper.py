#Web scraping script to get the top 10 movies from IMDb
import requests
import bs4


#scrape the information
def getContents(soup):
        contents = dict()
        
        #loop through top 10 movies' content
        for heading in soup.findAll("div","lister-item-content")[:10]:
                #get the movie title
                movie = heading.find("h3", "lister-item-header").text
                contents[movie] = []
                
                #get movie summary and additional information
                extra = heading.findAll("p")
                contents[movie].append(extra[0].find("span", "runtime").text)
                contents[movie].append(extra[0].find("span", "genre").text)
                contents[movie].append(extra[1].text)
                contents[movie].append(heading.find("strong").text)
                
                #get movie crew
                crew = []
                for actor in extra[2].findAll("a"):
                        crew.append(actor.text)
                contents[movie].append(crew)
                
        return contents                


#show the contents
def showContents(contents):
        for i in contents:
                title = i.split("\n")
                
                print(" ".join(c for c in title[1:]))
                print("Genre : " + contents[i][1].strip() + "\t" + "Runtime : " + contents[i][0])
                print("Movie summary : " + contents[i][2].strip())
                print("IMDb Rating : " + contents[i][3] + "/10")
                
                print("Director : " + contents[i][4][0])
                print("Stars : " + ", ".join(c for c in contents[i][4][1:]))
                print("\n")
        
        

if __name__ == '__main__':
        #get the webpage and convert it to a BeautifulSoup object
        req = requests.get("https://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012")
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        
        #print the title
        print(soup.title.text + "\n\n")
        
        contents = getContents(soup)
        showContents(contents)
