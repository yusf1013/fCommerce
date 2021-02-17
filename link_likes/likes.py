import sys

import requests
import bs4
import re


def get_likes(soup):
    f = soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
    if f is not None:
        likes = f.find('span', attrs={'class': '_52id _50f5 _50f7'})  # finding span tag inside class
        # print(likes.text)
        lik = likes.text.split(" „")[0]
        lik = lik.replace(".", "")
        # lik = lik[0:len(link)-1]
        return lik
    return ""


def get_soup(current_link, s):
    res = requests.get(current_link)
    result = re.search(s, res.text)

    if result or s == 'skip':
        return bs4.BeautifulSoup(res.text, 'lxml')
    else:
        return None


newFile = open("test3.txt", encoding="utf-8")
outFile = open("link_likes.csv", "a", encoding="utf-16")
newList = newFile.readlines()
print("Total: ", len(newList))
totalLinks = len(newList)

try:
    f = open('done_link_likes.txt', 'r')
    doneList = f.readlines()
    f.close()
except:
    doneList = []

print("Already done: ", len(doneList))
f = open('done_link_likes.txt', 'a')

start = 0
end = totalLinks
if len(sys.argv) == 2:
    a = int(sys.argv[0])
    b = int(sys.argv[1])
    start = totalLinks // b * (a - 1)
    end = totalLinks // b * a
    newList = newList[start:end]


for link in newList:
    done = link
    if done in doneList:
        continue

    link = link[0:len(link) - 1]
    res = link + ", "
    soup = get_soup(link, 'skip')
    likes = get_likes(soup)
    res += likes + "\n"
    print(res)
    outFile.writelines(res)
    outFile.flush()
    doneList.append(done)
    f.write(done)
    f.flush()
