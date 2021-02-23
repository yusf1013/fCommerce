import sys
import re, random
import requests
import bs4
import re


def keep_num(str):
    ans = re.sub("[^0-9]", "", str)
    ans = ans.replace(".", "")
    return ans


def get_likes(soup):
    f = soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
    if f is not None:
        likes = f.find('span', attrs={'class': '_52id _50f5 _50f7'})  # finding span tag inside class
        # print(likes.text)
        # lik = likes.text.split(" „")[0]
        # lik = lik.replace(".", "")
        # lik = lik[0:len(link)-1]
        lik = likes.text
        lik = keep_num(lik)
        return lik
    return ""


def get_soup(current_link, s):
    # print(current_link)
    res = requests.get(current_link)
    result = re.search(s, res.text)

    if result or s == 'skip':
        return bs4.BeautifulSoup(res.text, 'lxml')
    else:
        return None


newFile = open("test3.txt", encoding="utf-8")
outFile = open("link_likes.csv", "a", encoding="utf-8")
newList = newFile.readlines()
newList = newList[9761:]
print("Total: ", len(newList))
totalLinks = len(newList)

doneFile = open("link_likes.csv", "r", encoding="utf-8")
doneFileList = doneFile.readlines()
doneFile.close()

"""try:
    f = open('done_link_likes.txt', 'r')
    doneList = f.readlines()
    f.close()
except:
    doneList = []"""

doneList = []
for link in doneFileList:
    doneList.append(link.split(",")[0])
    # print(link.split(",")[0])


print("Already done: ", len(doneList))
# f = open('done_link_likes.txt', 'a', encoding="utf-8")

start = 0
end = totalLinks
print(len(sys.argv))
print(sys.argv)
if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    start = totalLinks // b * (a - 1)
    end = totalLinks // b * a
    newList = newList[start:end]
else:
    random.shuffle(newList)
    # newList = newList[:5]

count = start
print("start, end: ", start, end)

for link in newList:
    count += 1
    print(count, link)

    done = link
    if link[0:len(link)-1] in doneList:
        continue

    link = link[0:len(link) - 1]
    res = link + ", "
    soup = get_soup(link, 'skip')
    likes = get_likes(soup)
    if likes != "":
        res += likes + "\n"
        print(res)
        outFile.writelines(res)
        outFile.flush()
        doneList.append(done)
        # f.write(done)
        # f.flush()
    else:
        print("failed: ", link)
