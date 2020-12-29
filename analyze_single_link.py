import time
import requests
import bs4
import re


def main():
    # first_link = 'https://www.facebook.com/GFOBD'
    # first_link = 'https://www.facebook.com/techlandbd'
    # first_link = 'https://www.facebook.com/Bro889'
    # first_link = "https://www.facebook.com/DoctorTasnimJara/about"
    # first_link = "https://www.facebook.com/pg/techlandbd/about"
    # first_link = "https://www.facebook.com/ClickersLab/about"
    # first_link = "https://www.facebook.com/GadgetClub.com.BD"
    # first_link = "https://www.facebook.com/21march2017"
    # first_link = "https://www.facebook.com/pg/21march2017/post"
    first_link = "https://www.facebook.com/utsahoSobujayon"
    preferred_size = 1

    arr = [first_link]
    temp = 0

    # write_header()
    while temp < len(arr):

        current_link = arr[temp]
        keyword = current_link.split('.com/')[1]
        soup = get_soup(current_link, 'skip')

        if soup is not None:
            print(str(temp + 1) + ': ', current_link)
            extract_info(soup, current_link)
        temp += 1
    print("done")


def get_soup(current_link, s):
    print("in get soup")
    res = requests.get(current_link)
    result = re.search(s, res.text)

    if result or s == 'skip':
        return bs4.BeautifulSoup(res.text, 'lxml')
    else:
        return None


def extract_info(soup, link):
    keyword = link.split('.com/')[1]

    print("___________________________________________________________________________________________________________")
    for shit in soup.find_all('div', class_=True):
        """test_list = ['price', 'tk', 'taka', '£', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier',
                     'প্রোডাক্ট', 'ডেলিভারি', 'অর্ডার', 'বিকাশ'] """
        test_list = ['price', 'order', 'delivery', 'bkash', 'rocket', 'nagad', 'courier', 'ডেলিভারি', 'অর্ডার']

        # condition = 'ডেলিভারি ' in shit.text
        condition = any(ele in shit.text.lower() for ele in test_list)
        if condition:
            print(shit['class'], shit.text)
            print("\n\n\n")
        else:
            print(shit.text)


    """for shit in soup.find_all('a', class_=True):
        a = str(shit['class'])
        if a == "['_2js3']":
            print(shit.text)
        else:
            print(a)"""


main()
