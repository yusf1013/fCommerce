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

def get_soup(current_link, s):
    res = requests.get(current_link)
    result = re.search(s, res.text)

    if result or s == 'skip':
        return bs4.BeautifulSoup(res.text, 'lxml')
    else:
        return None



def is_ecommerce(shit):
    """test_list = ['price', 'tk', 'taka', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier',
                 'প্রোডাক্ট', 'ডেলিভারি', 'অর্ডার', 'বিকাশ', 'দাম', 'টাকা']"""

    test_list = ['price', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier', 'Price', 'Order', 'Delivery',
                 'Bkash', 'Rocket', 'Nagad', 'Courier', 'ডেলিভারি', 'অর্ডার']
    condition = 0

    for item in test_list:
        if re.search(r'\b%s\b' % item, shit.text):
            #print("---" + item + "---")
            # print(shit.text)
            condition += 1
            break

    return condition


def is_jobsite(shit):
    test_list = ["Hiring", "hiring", "job", "Job", "employee", "Employee", "Employer", "chakri", "Chakri", "Internship",
                 "internship", "চাকরি", "Salary", "salary", "চাকরির বিজ্ঞপ্তি", "job circular", "Job circular",
                 "Job Circular", "নিয়োগ বিজ্ঞপ্তি", "Job Opportunity", "Job opportunity", "job opportunity"]
    # condition = '7,957' in shit.text
    # condition = any(ele in shit.text.lower() for ele in test_list)
    # condition = False
    condition = 0

    for item in test_list:
        if re.search(r'\b%s\b' % item, shit.text):
            # print("---" + item + "---")
            # print(shit.text)
            condition += 1
            break
    return condition


def getExistence(link):
    keyword = link.split('.com/')[1]
    link = "https://www.facebook.com/pg/" + keyword + "/posts/"
    soup = get_soup(link, 'skip')
    if soup is not None:
        # flag = False
        total = 0
        # for shit in soup.find_all('div', class_=True):
        for shit in soup.find_all('div'):
            condition = is_ecommerce(shit)
            condition2 = is_jobsite(shit)
            total = max(total, condition)
            if condition2 != 0:
                print("Its a Job Site")
                return 0

            if condition != 0:
                print("Yaa Its a E-commerce Site.")
                return 1

        print("Its neither e-commerce nor job site")
    return 0


startGlobal = 1885
if __name__ == '__main__':
    with open("onlyEcommercePageLinks.txt", "a", 2, encoding="utf-8")as onlyEcommercePageLinks:
        Input = open("linksGotFromYusuf.txt", "r", encoding='utf-8')
        TemporaryInput = open("onlyEcommercePageLinks.txt", "r", encoding='utf-8')
        List = Input.readlines()
        TemporaryList = TemporaryInput.readlines()
        start = startGlobal
        end = len(List)
        # Set.update(List)
        # if len(List) > start + 1000:
        #     end = start + 1000
        List = List[start: end]
        temp = startGlobal
        success_count = 0
        for oneLine in List:
            temp += 1
            print(str(temp) + "." + oneLine)
            if oneLine.strip() in TemporaryList or oneLine in TemporaryList:
                continue
            oneLine = oneLine.split("\n")[0]

            c = getExistence(oneLine)
            if c != 1:
                continue
            success_count += c
            print(success_count, "(Success)/ " + str(temp-startGlobal) + "(Total)")
            sys.stdout.flush()
            onlyEcommercePageLinks.write(str(oneLine) + "\n")
            onlyEcommercePageLinks.flush()
            os.fsync(onlyEcommercePageLinks.fileno())

        TemporaryInput.close()
        Input.close()
        onlyEcommercePageLinks.close()

