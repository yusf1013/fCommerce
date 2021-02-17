# import requests
# import bs4
# import re
# import os
# import os.path
# import lxml
# import time
# from os import path
# import sys
# import time
# import datetime
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
#
#
# def get_soup(current_link, s):
#     res = requests.get(current_link)
#     result = re.search(s, res.text)
#
#     if result or s == 'skip':
#         return bs4.BeautifulSoup(res.text, 'lxml')
#     else:
#         return None
#
#
# def getPhoneNumber(link):
#     link += "/about"
#     keyword = link.split('.com/')[1]
#     phone = ""
#
#     soup = get_soup(link, 'skip')
#     if soup is not None:
#         for shit in soup.find_all('div', class_=True):
#             condition = ("['_4bl9']" in str(shit['class']) or "['_50f4']" in str(shit['class'])) and "Call" in str(shit.text)
#             if condition:
#                     #print(str(shit['class']).strip(), shit.text)
#                     phone = shit.text
#     return phone
# def get_cat_from_soup(soup):
#     for shit in soup.find_all('div', class_=True):
#         aaa = str(shit['class'])
#         try:
#             if aaa == "['clearfix', '_ikh']":
#                 itemm = str(shit)
#                 if 'LwDWwC1d0Rx' in itemm:
#                     print(shit.text)
#                     return shit.text
#         except AttributeError:
#             return ""
#
#
#     return ""
#
#
# def is_ecommerce(shit):
#     """test_list = ['price', 'tk', 'taka', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier',
#                  'প্রোডাক্ট', 'ডেলিভারি', 'অর্ডার', 'বিকাশ', 'দাম', 'টাকা']"""
#
#     test_list = ['price', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier', 'Price', 'Order', 'Delivery',
#                  'Bkash', 'Rocket', 'Nagad', 'Courier', 'ডেলিভারি', 'অর্ডার']
#     condition = 0
#
#     for item in test_list:
#         if re.search(r'\b%s\b' % item, shit.text):
#             #print("---" + item + "---")
#             # print(shit.text)
#             condition += 1
#             break
#
#     return condition
#
#
# def is_jobsite(shit):
#     test_list = ["Hiring", "hiring", "job", "Job", "employee", "Employee", "Employer", "chakri", "Chakri", "Internship",
#                  "internship", "চাকরি", "Salary", "salary", "চাকরির বিজ্ঞপ্তি", "job circular", "Job circular",
#                  "Job Circular", "নিয়োগ বিজ্ঞপ্তি", "Job Opportunity", "Job opportunity", "job opportunity"]
#     # condition = '7,957' in shit.text
#     # condition = any(ele in shit.text.lower() for ele in test_list)
#     # condition = False
#     condition = 0
#
#     for item in test_list:
#         if re.search(r'\b%s\b' % item, shit.text):
#             # print("---" + item + "---")
#             # print(shit.text)
#             condition += 1
#             break
#     return condition
#
# #
# # def getExistence(link):
# #     keyword = link.split('.com/')[1]
# #     link = "https://www.facebook.com/pg/" + keyword + "/posts/"
# #     soup = get_soup(link, 'skip')
# #     if soup is not None:
# #         # flag = False
# #         total = 0
# #         # for shit in soup.find_all('div', class_=True):
# #         for shit in soup.find_all('div'):
# #             condition = is_ecommerce(shit)
# #             condition2 = is_jobsite(shit)
# #             total = max(total, condition)
# #             if condition2 != 0:
# #                 print("Its a Job Site")
# #                 return 0
# #
# #             if condition != 0:
# #                 print("Yaa Its a E-commerce Site.")
# #
# #                 return 1
# #
# #         print("Its neither e-commerce nor job site")
# #     return 0
#
#
# Set = set()
# s = 'Bangladesh'
# startGlobal =2100
# #  This number should be changed
#
# fortyK = open("yusuf2.txt", "r", encoding='utf-8')
# fortyKList = fortyK.readlines()
# newButDiscoveredAlready = open("newlyDiscover.txt", "r", encoding='utf-8')
# newButDiscoveredAlreadyList = newButDiscoveredAlready.readlines()
# currentlyInventedLinkList=['https://www.facebook.com/RemoraTTH']
# if __name__ == '__main__':
#     with open("newlyDiscover.txt", "a", 2, encoding="utf-8")as newlyDiscoveredButNotAdded:
#         with open("testlinks.txt", "a", 2, encoding="utf-8") as f:
#             with open("Result.txt", "a", encoding="utf-8") as csvFile:
#                 with open("E-commerceButNotWriten.txt", "a", encoding="utf-8") as ecommerceButNotGotAnyPost:
#                     success_count = 0
#                     total_count = 0
#                     if path.exists("Result.csv"):
#                         print("")
#                     else:
#                         csvFile.write("Page Name   \t,   Page Link    \t, Contact  \t, Page Likes  \t, Last Post  \t, 2nd Last Post  \t, 3rd Last Post   \t, 4th Last Post   \t,   5th Last Post   \n")
#                     while True:
#                         input = open("testlinks.txt", "r", encoding='utf-8')
#                         List = input.readlines()
#                         Set.update(List)
#                         print("test link unique links= "+str(len(Set)))
#                         willNewlyAddInTextLinks = 0
#                         start = startGlobal
#                         end = len(List)
#                         if len(List) > start+1000:
#                             end = start + 1000
#                         List = List[start: end]
#                         temp = startGlobal
#                         for oneLine in List:
#                             temp = temp + 1
#                             #####################################################
#                             if oneLine.strip() in newButDiscoveredAlreadyList or oneLine in newButDiscoveredAlreadyList:
#
#                                 print("contains in newButDiscoveredAlreadyList:"+str(oneLine)+"\n")
#                                 continue
#
#                             if oneLine in currentlyInventedLinkList or oneLine.strip() in currentlyInventedLinkList:
#                                 print("contains in currentlyInventedLinkList:" + str(oneLine) + "\n")
#                                 continue
#
#                             if oneLine.strip() in fortyKList or oneLine in fortyKList:
#
#                                 print("yes contains in fortyKList:"+str(oneLine)+"\n")
#                                 continue
#                             #####################################################
#                             currentlyInventedLinkList.append(oneLine)
#                             newlyDiscoveredButNotAdded.write(str(oneLine))
#                             newlyDiscoveredButNotAdded.flush()
#                             os.fsync(newlyDiscoveredButNotAdded.fileno())
#                             print(str(temp)+"."+oneLine)
#                             link = oneLine
#                             link = link.split("\n")[0]
#                             c = 0
#                             keyword = link.split('.com/')[1]
#                             link = "https://www.facebook.com/pg/" + keyword + "/posts/"
#                             res = requests.get(link)
#                             SingleCallSoup = bs4.BeautifulSoup(res.text, 'lxml')
#                             time.sleep(3)
#                             if SingleCallSoup is not None:
#                                 for shit in SingleCallSoup.find_all('div'):
#                                     condition = is_ecommerce(shit)
#                                     condition2 = is_jobsite(shit)
#                                     if condition2 != 0:
#                                         c = 0
#                                     if condition != 0:
#                                         c = 1
#                             if c != 1:
#                                 print("Its either shit site or job site")
#                                 continue
#                             else:
#                                 print("Yaa Its a E-commerce Site.")
#                             success_count += c
#                             print(success_count, "(Success)/ " + str(temp-startGlobal) + "(Total)")
#                             ########
#                             phone_number = ""
#                             lol = str(getPhoneNumber(oneLine.split("\n")[0]))
#                             try:
#                                 phone_number = lol.split("Call ")[1]
#                                 phone_number = phone_number.replace(",", "")
#                             except IndexError:
#                                 phone_number = ""
#                             #####
#                             csvText = ""
#                             dictionary = {}
#                             info = {
#                                 'link': oneLine.strip(),
#                                 'phone': phone_number,
#                                 'name': (str(oneLine.split('.com/')[1])).strip(),
#                                 'pageLikes': "",
#                                 'category': "",
#                             }
#                             res = requests.get(oneLine)
#                             result = re.search(s, res.text)
#                             soup = bs4.BeautifulSoup(res.text, "html.parser")
#                             info['category'] = get_cat_from_soup(soup)
#                             # time.sleep(1)
#                             for link in soup.find_all('a', href=True):
#                                 a = str(link['href'])
#                                 if "/?ref=py_c" in a:
#                                     b = a.replace("/?ref=py_c", '')
#                                     if b not in Set:
#                                         willNewlyAddInTextLinks += 1
#                                         # print(str(b))
#                                         f.write(b)
#                                         f.write('\n')
#                                         Set.add(b)
#                             f.flush()
#                             os.fsync(f.fileno())
#                             soup = bs4.BeautifulSoup(res.text, 'lxml')
#                             # soup = bs4.BeautifulSoup(res.text, "html.parser")
#                             # soup = SingleCallSoup
#                             try:
#                                 full_oc_crap = soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
#                                 likes = full_oc_crap.find('span', attrs={'class': '_52id _50f5 _50f7'})
#                                 temper = str(likes.text)
#                                 temper = temper.replace(",", "")
#                                 info['pageLikes'] = temper
#                             except AttributeError:
#                                 likes = ""
#                                 info['pageLikes'] = likes
#                             forThoseWhoAreEcommerceButNotShowingAnyPost = ""
#
#                             for link in soup.find_all('abbr', ):
#                                 output = link['title']
#                                 forThoseWhoAreEcommerceButNotShowingAnyPost += str(link)
#                                 x = output.split()
#                                 ########################
#                                 if len(x) != 6:
#                                     x.pop()
#                                     x[1], x[2]=x[2], x[1]
#                                 x[1] = x[1].replace(",", "")
#                                 # print("Details = "+str(x))
#                                 #######################
#
#                                 x[0] = x[0].replace(",", "")
#                                 month = months.index(x[2])
#                                 hourMinute = x[len(x)-1]
#                                 minute = str(hourMinute).split(":")[1]
#                                 value = int(x[3]) * 3000 + (month + 1) * 100 + int(x[1])+int(minute)
#                                 dictionary[value] = output
#                             keyword = oneLine.split('.com/')[1]
#                             for link in soup.find_all('a', href=True):
#                                 a = str(link['href'])
#                                 if keyword in a and 'facebook' in a and 'hc_ref' in a and len(link.text) > 1:
#                                     info['name'] = link.text
#                             stringList = []
#                             List = list(dictionary.items())
#                             List.sort(reverse=True)
#                             for i in range(3):
#                                 try:
#                                     string = (List[i])[1]
#                                     string = string.replace(",", "")
#                                 except IndexError:
#                                     string = ""
#                                 stringList.append(string)
#                             csvText += info['name'] + ",\t"+info['category'] + ",\t" + info['link'] + ",\t" + info['phone'] + ",\t" + info['pageLikes'] + ",\t" + stringList[0] + ",\t" \
#                                        + stringList[1] + ",\t" + stringList[2]+"\n"
#
#                             print(csvText)
#
#                             # print("string list= "+str(stringList)+ "  || "+stringList[1])
#                             if len(stringList[1])>3:
#                                 sys.stdout.flush()
#                                 csvFile.write(str(csvText))
#                                 csvFile.flush()
#                                 os.fsync(csvFile.fileno())
#                             else:
#                                 print("Not found beautiful parser.For lack of info its not added in Result.txt.")
#                                 print(forThoseWhoAreEcommerceButNotShowingAnyPost)
#                                 ecommerceButNotGotAnyPost.write(str(oneLine))
#
#                         print('testLinks ( '+str(start)+" - "+str(end)+' ) pora shes hoise')
#                         print("Newly added unique links in testlinks = "+str(willNewlyAddInTextLinks))
#                         startGlobal = end
#                         f.flush()
#                         Set = set()
#                         input.close()
#         ecommerceButNotGotAnyPost.close()
#         csvFile.close()
#         f.close()
#     newlyDiscoveredButNotAdded.close()
#     newButDiscoveredAlready.close()
#     fortyK.close()

Set=set()
with open("onDuplicateLink.txt", "a", 2, encoding="utf-8")as suggestedPages:
    Input = open("suggestedPages.txt", "r", encoding='utf-8')
    List=Input.readlines()
    for oneLink in List:
        if oneLink not in Set:
            Set.add(oneLink)

            suggestedPages.write(oneLink)
        else:
            print(oneLink)
    print(len(Set))
    Input.close()
    suggestedPages.close()