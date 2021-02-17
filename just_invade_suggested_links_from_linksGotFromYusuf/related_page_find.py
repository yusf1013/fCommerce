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
startGlobal = 13100
Set = set()
with open("suggestedPages.txt", "a", 2, encoding="utf-8")as suggestedPages:
    Input = open("linksGotFromYusuf.txt", "r", encoding='utf-8')
    TemporaryInput = open("suggestedPages.txt", "r", encoding='utf-8')
    SecondTemporaryInput = open("yusuf2.txt", "r", encoding='utf-8')
    List = Input.readlines()
    forOnlyOnePurpose = List
    TemporaryList = TemporaryInput.readlines()
    SecondTemporaryList=SecondTemporaryInput.readlines()
    print(len(Set))
    start = startGlobal
    end = len(List)
    List = List[start: end]
    temp = startGlobal
    for oneLine in List:
        temp += 1
        print(str(temp)+"."+oneLine)
        oneLine = oneLine.split("\n")[0]
        res = requests.get(oneLine)
        SingleCallSoup = bs4.BeautifulSoup(res.text,  "html.parser")
        time.sleep(2.5)
        isThereAnyHelpfulLink = True
        for link in SingleCallSoup.find_all('a', href=True):
            a = str(link['href'])
            if "/?ref=py_c" in a:
                b = a.replace("/?ref=py_c", '')
                if isThereAnyHelpfulLink:
                    print("True")
                isThereAnyHelpfulLink = False

                if b in TemporaryList or b in SecondTemporaryList or b in forOnlyOnePurpose:
                    continue
                if b.strip() in TemporaryList or b.strip() in SecondTemporaryList or b.strip() in forOnlyOnePurpose:
                    continue
                if b not in Set:

                    suggestedPages.write(b)
                    suggestedPages.write('\n')
                    Set.add(b)

        suggestedPages.flush()
        os.fsync(suggestedPages.fileno())
    Input.close()
    TemporaryInput.close()
    SecondTemporaryInput.close()
    suggestedPages.close()
