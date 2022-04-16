import requests
from bs4 import BeautifulSoup
url = "https://github.com/"

r = requests.get(url)
htmlcontent = r.content
#print(htmlcontent)

soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify)

title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))

paras = soup.find_all('p')
print(paras)

print(soup.find('p'))
print(soup.find('p')['class'])

print(soup.find_all('p', class_="lead"))

print(soup.find('p').get_text())
print(soup.get_text())


anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        link = ("https://github.com/",link.get('herf'))
        all_links.add(link)
        print(link)

markup = "<p><!--this is comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

navbarSupportContent = soup.find(id)
for ele in navbarSupportContent.contents:
    print(ele)

for item in navbarSupportContent.strings:
    print(item)
for item in navbarSupportContent.stripped_strings:
    print(item)

print(navbarSupportContent.parent)
for item in navbarSupportContent.parents:
    print(item.name)

print(navbarSupportContent.next_sibling.next_sibling)
print(navbarSupportContent.previous_sibling.previous_sibling)