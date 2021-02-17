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

startGlobal = 0
with open("FreshLinks.txt", "a", 2, encoding="utf-8")as FreshLinks:
        Input = open("suggestedPages.txt", "r", encoding='utf-8')
        TemporaryInput = open("linksGotFromYusuf.txt", "r", encoding='utf-8')
        SecondTemporaryInput = open("yusuf2.txt", "r", encoding='utf-8')
        List = Input.readlines()
        TemporaryInputList = TemporaryInput.readlines()
        SecondTemporaryInputList=SecondTemporaryInput.read()
        start = startGlobal
        end = len(List)
        currentlyUsing = List[start: end]
        temp = startGlobal
        for oneLine in currentlyUsing:

            temp += 1
            print(temp)
            if oneLine.strip() in TemporaryInputList or oneLine in TemporaryInputList:
                continue
            if oneLine.strip() in SecondTemporaryInputList or oneLine in SecondTemporaryInputList:
                continue

            oneLine = oneLine.split("\n")[0]

            sys.stdout.flush()
            FreshLinks.write(str(oneLine)+"\n")
            FreshLinks.flush()
            os.fsync(FreshLinks.fileno())

        Input.close()
        TemporaryInput.close()
        SecondTemporaryInput.close()
        FreshLinks.close()
