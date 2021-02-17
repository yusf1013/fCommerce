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


s = 'Bangladesh'
startGlobal = 0
with open("LinksWithFivePosts.txt", "a", 2, encoding="utf-8")as LinksWithFivePosts:
    with open("alreadyDiscoveredLinksLastFivePosts.txt", "a", 2, encoding="utf-8")as alreadyDiscoveredLinks:
        Input = open("onlyEcommercePageLinks.txt", "r", encoding='utf-8')
        TemporaryInput = open("alreadyDiscoveredLinksLastFivePosts.txt", "r", encoding='utf-8')
        List = Input.readlines()
        TemporaryInputList = TemporaryInput.readlines()
        start = startGlobal
        end = len(List)
        # if len(List) > start + 1000:
        #     end = start + 1000
        currentlyUsing = List[start: end]
        temp = startGlobal
        for oneLine in currentlyUsing:
            temp = temp + 1
            print(str(temp) + "." + oneLine)
            if oneLine.strip() in TemporaryInputList or oneLine in TemporaryInputList:
                continue

            oneLine = oneLine.split("\n")[0]
            keyword = oneLine.split('.com/')[1]
            # print("Key = "+str(keyword))
            link = "https://www.facebook.com/pg/" + keyword + "/posts/"
            res = requests.get(link)
            SingleCallSoup = bs4.BeautifulSoup(res.text, 'lxml')
            # time.sleep(1)
            dictionary = {}
            CsvText = str(oneLine)
            for oneDiv in SingleCallSoup.find_all('abbr', ):
                output = oneDiv['title']
                x = output.split()
                # print(output)
                if len(x) != 6:
                    x.pop()
                    x[1], x[2] = x[2], x[1]
                x[1] = x[1].replace(",", "")
                # print("Details = "+str(x))
                #######################

                x[0] = x[0].replace(",", "")
                month = months.index(x[2])
                hourMinute = x[len(x) - 1]
                minute = str(hourMinute).split(":")[1]
                value = int(x[3]) * 3000 + (month + 1) * 100 + int(x[1]) + int(minute)
                dictionary[value] = output
            # print("len dictionary="+str(len(dictionary)))

            List = list(dictionary.items())
            List.sort(reverse=True)
            for i in range(8):
                try:
                    string = (List[i])[1]
                    string = string.replace(",", "")
                    CsvText += ",\t"+string
                except IndexError:
                    string = ""
                    CsvText += ",\t" + string

            print(CsvText)
            sys.stdout.flush()
            LinksWithFivePosts.write(CsvText+"\n")
            LinksWithFivePosts.flush()
            os.fsync(LinksWithFivePosts.fileno())

            alreadyDiscoveredLinks.write(str(oneLine) + "\n")
            alreadyDiscoveredLinks.flush()
            os.fsync(alreadyDiscoveredLinks.fileno())

        LinksWithFivePosts.close()
        Input.close()
        LinksWithFivePosts.close()
