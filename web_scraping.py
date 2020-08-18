from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.imdb.com/list/ls070150896/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"lister-item-content"})

starwars_movies = []
for container in containers:
    name = container.h3.a.text
    year = container.find("span",{"class":"lister-item-year text-muted unbold"}).text
    rating = container.find("span",{"class":"ipl-rating-star__rating"}).text
    dict = {"name":name , "year":year , "rating":rating}
    starwars_movies.append(dict)
count = 1
for i in starwars_movies:
    print("------%d------"%(count))
    print("Name: %s"%(i["name"]))
    print("Year: %s"%(i["year"]))
    print("Rating: %s"%(i["rating"]))
    count += 1
