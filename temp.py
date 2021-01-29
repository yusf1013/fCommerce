import random
import requests
import bs4
import re


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
    # test_list = ["Hiring","hiring", "job","Job", "employee","Employee", "Employer","chakri","Chakri", "Internship","internship", "চাকরি", "Salary","salary", "চাকরির বিজ্ঞপ্তি", "job circular","Job circular","Job Circular", "নিয়োগ বিজ্ঞপ্তি", "Job Opportunity", "Job opportunity", "job opportunity"]
    # condition = '7,957' in shit.text
    # condition = any(ele in shit.text.lower() for ele in test_list)
    # condition = False
    condition = 0

    for item in test_list:
        if " " + item + "" in shit.text:
            print("---" + item + "---")
            # print(shit.text)
            condition += 1
            # if condition == 1:
            #     return 1
            break

    return condition


def is_jobsite(shit):
    """test_list = ['price', 'tk', 'taka', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier',
                 'প্রোডাক্ট', 'ডেলিভারি', 'অর্ডার', 'বিকাশ', 'দাম', 'টাকা']"""

    # test_list = ['price', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier', 'ডেলিভারি', 'অর্ডার']
    test_list = ["Hiring", "hiring", "job", "Job", "employee", "Employee", "Employer", "chakri", "Chakri", "Internship",
                 "internship", "চাকরি", "Salary", "salary", "চাকরির বিজ্ঞপ্তি", "job circular", "Job circular",
                 "Job Circular", "নিয়োগ বিজ্ঞপ্তি", "Job Opportunity", "Job opportunity", "job opportunity"]
    # condition = '7,957' in shit.text
    # condition = any(ele in shit.text.lower() for ele in test_list)
    # condition = False
    condition = 0

    for item in test_list:
        if " " + item + "" in shit.text:
            print("---" + item + "---")
            # print(shit.text)
            condition += 1
            break

    return condition


def phone(shit):
    # condition = ("['_4bl9']" in str(shit['class']) or "['_50f4']" in str(shit['class'])) and "Call" in str(shit.text)
    print(shit.text)
    condition = '_4-u3 _5sqi _5sqk' in str(shit['class'])

    if condition:
        return 1
    return 0


def getExistence(link):
    keyword = link.split('.com/')[1]
    # link = "https://www.facebook.com/pg/" + keyword + "/posts/"

    count = 0
    soup = get_soup(link, 'skip')
    if soup is not None:
        # flag = False
        total = 0
        for shit in soup.find_all('div', class_=True):
        # for shit in soup.find_all('div'):
            # condition = ("['_4bl9']" in str(shit['class']) or "['_50f4']" in str(shit['class'])) and "Call" in str(shit.text)
            # condition = "['_2pi9', '_2pi2']" in str(shit['class']) # this is for about section
            # condition = "£" in str(shit.text)
            # condition = is_ecommerce(shit)
            condition = phone(shit)
            # condition2 = is_jobsite(shit)
            total = max(total, condition)

            if condition != 0:
                print(str(shit['class']).strip(), shit.text)
                print("\n\n\n")
                flag = True

                # break
            """else:
                print(str(shit['class']).strip(), shit.text)"""

        if total != 0:
            count += 1
        print("total: " + str(total))
    return count


def run_by_range(start, end, random):
    count = 0
    count2 = 0
    input = open("yusuf2.txt", "r", encoding='utf-8')
    link_list = input.readlines()

    if random:
        random.shuffle(link_list)
    link_list = link_list[start - 1: end]
    for link in link_list:
        link = link.split("\n")[0]
        link += "/about"
        print(str(start + count2 + 1) + ". " + link)
        c = (getExistence(link))
        count += c
        count2 += 1
        print(c)
        print(count, "/ " + str(count2))
    # print(count, "/ " + str((end - start)))


def run_from_list(number_list):
    success_count = 0
    total_count = 0
    input = open("yusuf2.txt", "r", encoding='utf-8')
    link_list = input.readlines()

    for number in number_list:
        link = link_list[int(number) - 1]
        link = link.split("\n")[0]
        print(str(number) + ". " + link)
        c = (getExistence(link))
        success_count += c
        total_count += 1
        print(c)
        print(success_count, "/ " + str(total_count))


#  print(success_count, "/ " + str(len(number_list)))


if __name__ == '__main__':
    # test numbers from serial 20 to 22 inclusive. No need to subtract 1
    run_by_range(201, 201, False)
    # test numbers form list. No need to subtract 1
    # run_from_list([1, 5, 7])
