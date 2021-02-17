import requests
import bs4
import re

def get_cat_from_soup(soup):
    for shit in soup.find_all('div', class_=True):
        a = str(shit['class'])
        if str(shit.text).startswith("categor"):
            item = str(shit)
            # print(shit.text)
            return shit.text[10:]

    return ""


def getPhoneNumber(soup):
    """link += "/about"
    keyword = link.split('.com/')[1]
    phone = ""

    soup = get_soup(link, 'skip')"""
    phone = ""
    if soup is not None:
        for shit in soup.find_all('div', class_=True):
            condition = ("['_4bl9']" in str(shit['class']) or "['_50f4']" in str(shit['class'])) and "Call " in str(shit.text)
            if condition:
                    # print(str(shit['class']).strip(), shit.text)
                    phone = shit.text.split("Call ")[1]
                    # print(phone)
    return phone


def get_soup(current_link, s):
    res = requests.get(current_link)
    result = re.search(s, res.text)

    if result or s == 'skip':
        return bs4.BeautifulSoup(res.text, 'lxml')
    else:
        return None


newFile = open("/test3.txt", encoding="utf-8")
outFile = open("link_cat_phone.csv", "a", encoding="utf-16")
newList = newFile.readlines()
print("Total: ", len(newList))

try:
    f = open('done_link_cat_phone.txt', 'r')
    doneList = f.readlines()
    f.close()
except:
    doneList = []

print("Already done: ", len(doneList))
f = open('done_link_cat_phone.txt', 'a')

for link in newList:
    done = link
    if done in doneList:
        continue

    link = link[0:len(link)-1] + "/about"
    res = link[0:len(link)-6] + ", "
    soup = get_soup(link, 'skip')
    phone = getPhoneNumber(soup)
    cat = get_cat_from_soup(soup)

    res += cat + ", " + phone + "\n"
    print(res)
    outFile.writelines(res)
    outFile.flush()
    doneList.append(done)
    f.write(done)
    f.flush()
