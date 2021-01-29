import requests
import bs4
import re
import os

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
            print("---" + item + "---")
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
            print("---" + item + "---")
            # print(shit.text)
            condition += 1
            break

    return condition


def getExistence(link):
    keyword = link.split('.com/')[1]
    link = "https://www.facebook.com/pg/" + keyword + "/posts/"

    count = 0
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

        if total != 0:
            count += 1
        print("total: " + str(total))
    return count




Set = set()
s = 'Bangladesh'
startGlobal = 0  #  This number should be changed

fortyK = open("yusuf2.txt", "r", encoding='utf-8')
fortyKList = fortyK.readlines()


newButDiscoveredAlready = open("newlyDiscover.txt", "r", encoding='utf-8')
newButDiscoveredAlreadyList = newButDiscoveredAlready.readlines()


currentlyInventedLinkList=['https://www.facebook.com/RemoraTTH']
if __name__ == '__main__':

    with open("newlyDiscover.txt", "a", 2, encoding="utf-8")as newlyDiscoveredButNotAdded:
        with open("testlinks.txt", "a", 2, encoding="utf-8") as f:
            success_count = 0
            total_count = 0
            while True:

                input = open("testlinks.txt", "r", encoding='utf-8')
                List = input.readlines()
                start = startGlobal
                end = len(List)
             #   end = len(List)>1000? startGlobal+1000: len(List)
                List = List[start: end]
                temp = startGlobal

                for oneLine in List:
                    temp = temp + 1

                    #####################################################
                    if oneLine.strip() in newButDiscoveredAlreadyList or oneLine in newButDiscoveredAlreadyList:

                        print("contains in newButDiscoveredAlreadyList:"+str(oneLine)+"\n")
                        continue

                    if oneLine in currentlyInventedLinkList or oneLine.strip() in currentlyInventedLinkList:
                        print("contains in currentlyInventedLinkList:" + str(oneLine) + "\n")
                        continue

                    if oneLine.strip() in fortyKList or oneLine in fortyKList:

                        print("yes contains in fortyKList:"+str(oneLine)+"\n")
                        continue
                    #####################################################


                    currentlyInventedLinkList.append(oneLine)
                    newlyDiscoveredButNotAdded.write(oneLine)
                    newlyDiscoveredButNotAdded.flush()
                    os.fsync(newlyDiscoveredButNotAdded.fileno())

                    print(str(temp)+"."+oneLine)
                    link = oneLine
                    link = link.split("\n")[0]
                    c = (getExistence(link))
                    success_count += c
                    total_count += 1
                    print(c)
                    print(success_count, "/ " + str(total_count))
                    res = requests.get(oneLine)
                    result = re.search(s, res.text)
                    if result:
                        soup = bs4.BeautifulSoup(res.text, "html.parser")
                        for link in soup.find_all('a', href=True):
                            a = str(link['href'])
                            if "/?ref=py_c" in a:
                                b = a.replace("/?ref=py_c", '')
                                Set.add(b)

                        for n in Set:
                            singleLink=str(n)
                            f.write(singleLink)
                            f.write('\n')

                        f.flush()
                        os.fsync(f.fileno())

                #testLinks ekbar pora shes hoise
                startGlobal = end
                input.close()
        f.close()
    newlyDiscoveredButNotAdded.close()
    newButDiscoveredAlready.close()
    fortyK.close()
