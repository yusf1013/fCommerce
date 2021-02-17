import requests
import bs4
import re
import os
import os.path
import lxml
import time
from os import path
import sys
import time
import datetime
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def get_soup(current_link, s):
    res = requests.get(current_link)
    result = re.search(s, res.text)

    if result or s == 'skip':
        return bs4.BeautifulSoup(res.text, 'lxml')
    else:
        return None


def getPhoneNumber(link):
    link += "/about"
    keyword = link.split('.com/')[1]
    phone = ""

    soup = get_soup(link, 'skip')
    if soup is not None:
        for shit in soup.find_all('div', class_=True):
            condition = ("['_4bl9']" in str(shit['class']) or "['_50f4']" in str(shit['class'])) and "Call" in str(shit.text)
            if condition:
                    #print(str(shit['class']).strip(), shit.text)
                    phone = shit.text
    return phone

# def get_cat_from_soup(soup):
#     for shit in soup.find_all('div', class_=True):
#         a = str(shit['class'])
#         if str(shit.text).startswith("categor"):
#             item = str(shit)
#             print(shit.text)
#             return shit.text
#
#     return ""
def get_cat_from_soup(soup):
    for shit in soup.find_all('div', class_=True):
        aaa = str(shit['class'])
        try:
            if aaa == "['clearfix', '_ikh']":
                itemm = str(shit)
                if 'LwDWwC1d0Rx' in itemm:
                    # print(shit.text)
                    return shit.text
        except AttributeError:
            return ""
    return ""
s = 'Bangladesh'
startGlobal = 130
if __name__ == '__main__':
    with open("LinksWithOtherAttributes.txt", "a", 2, encoding="utf-8")as LinksWithOtherAttributes:
        with open("alreadyDiscoveredLinksGetOtherAttributes.txt", "a", 2, encoding="utf-8")as alreadyDiscoveredLinks:
            Input = open("onlyEcommercePageLinks.txt", "r", encoding='utf-8')
            TemporaryInput = open("alreadyDiscoveredLinksGetOtherAttributes.txt", "r", encoding='utf-8')
            List = Input.readlines()
            TemporaryInputList = TemporaryInput.readlines()
            start = startGlobal
            end = len(List)
            currentlyUsing = List[start: end]
            temp = startGlobal
            for oneLine in currentlyUsing:
                temp = temp + 1
                print(str(temp) + "." + oneLine)
                if oneLine.strip() in TemporaryInputList or oneLine in TemporaryInputList:
                    continue
                oneLine = oneLine.split("\n")[0]
                keyword = oneLine.split('.com/')[1]
                # print(keyword)
                resForOneLine = requests.get(oneLine)
                # time.sleep(2)
                # ------------Category---------
                SoupForCategory = bs4.BeautifulSoup(resForOneLine.text, "html.parser")
                category = get_cat_from_soup(SoupForCategory)
                # ------------Likes---------
                likes = ""
                # SoupForLikes = bs4.BeautifulSoup(resForOneLine.text, "lxml")
                # try:
                #     full_oc_crap = SoupForLikes.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
                #     likes = full_oc_crap.find('span', attrs={'class': '_52id _50f5 _50f7'})
                #     temper = str(likes.text)
                #     temper = temper.replace(",", "")
                #     likes = temper
                # except AttributeError:
                #     likes = ""
                # ------------Phone Number---------
                phone_number = ""
                # attributesOfPhone = str(getPhoneNumber(oneLine))
                # try:
                #     phone_number = attributesOfPhone.split("Call ")[1]
                #     phone_number = phone_number.replace(",", "")
                # except IndexError:
                #     phone_number = ""

                CsvText=oneLine+",\t"+category+",\t"+likes+",\t"+phone_number
                print(CsvText)

            TemporaryInput.close()
            Input.close()
            alreadyDiscoveredLinks.close()
            LinksWithOtherAttributes.close()