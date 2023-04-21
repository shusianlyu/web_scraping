# ----------------------------------------------------------------------
# Name:        scrape.py
# Purpose:     Homework 8 - practice web scraping
#
# Author(s): Jessie Lyu, An Tran
# ----------------------------------------------------------------------
"""
Extract name, phone number, email, and education from webpages

Given a starting URL and file, explore embedded URLs relating to people.
Extract the name, phone number, email, and education in order to write it to
the file, which is a .csv file.
"""

import urllib.request
import urllib.error
import bs4
import re
import sys
import os

# Enter your constants here
FIRST_URL = 'https://sjsu.edu/people/'


def read_url(url):
    """
    Open the given url and return the corresponding soup object.
    :param url:(string) - the address of the web page to be read
    :return: (Beautiful Soup object) corresponding Beautiful Soup
    object or None if an error is encountered.
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            url_bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    except Exception as other_err: # safer on the web
        print(f'Other error with url: {url}\n{other_err}')
    else:
        soup = bs4.BeautifulSoup(url_bytes,'html.parser')
        return soup


def get_people_links(url):
    """
    Read the given url and return the relevant referenced links.
    :param url:(string) - the address of the faculty index page
    :return: (list of strings) - the relevant people links
    """
    # Enter your code below and remove the pass statement
    soup = read_url(url)
    # bad soup
    if soup is None:
        return None
    # get all anchors
    anchors = soup('a')
    # filter out anchors
    # - need to have '/people/'
    # - and doesnt end with '/people/' (do not search the current original url
    relevant_links = [urllib.parse.urljoin(FIRST_URL, each_anchor['href']) for
                      each_anchor in anchors if '/people/' in
                      each_anchor.get('href', None) and not each_anchor[
            'href'].endswith('/people/')]
    return relevant_links


def extract_name(soup):
    """
    Extract the first and last name from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a tuple of strings representing the first and last names
    """
    # Enter your code below and remove the pass statement
    # names are in h1 headers
    h1s = soup('h1')
    if h1s:
        # strip leading spaces if any
        name = h1s[0].get_text().strip()
        # deal with names with commas
        if ',' in name:
            comma_index = name.index(',')
            # more than one comma (Lisa Ann Rauch)
            if name.count(',') >= 2:
                second_comma_index = name.index(',', comma_index + 1)
                first_name = name[comma_index + 1:second_comma_index].strip()
            # one comma (Michael Sneary)
            else:
                first_name = name[comma_index + 1:].strip()
            # last name is assumed always before first comma
            last_name = name[:comma_index].strip()
            return last_name, first_name
        # deal with two spaces, get rid of middle initial (Simon A Rodan)
        elif name.count(' ') >= 2:
            first_space_index = name.index(' ')
            last_space_index = name.rindex(' ')
            first_name = name[:first_space_index].strip()
            last_name = name[last_space_index + 1:].strip()
            return last_name, first_name
        # deal with one space
        elif ' ' in name:
            space_index = name.index(' ')
            first_name = name[:space_index].strip()
            last_name = name[space_index + 1:].strip()
            return last_name, first_name
        # very weird format, return empty strings
        else:
            return "", ""
    # return empty strings
    else:
        return "", ""


def extract_email(soup):
    """
    Extracts the first email from the bytes of a web page
    :param soup: (Beautiful Soup object) corresponding Beautiful Soup
    object
    :return: (String) email of person or empty string if not found
    """
    # Enter your code below and remove the pass statement
    # compile regex for emails
    regex = re.compile(r'@\S+(.edu|.com|.org)', re.IGNORECASE)
    all_emails = soup.find_all(string=regex)
    # if not empty return the first email found
    if all_emails:
        return all_emails[0].strip()
    else:
        return ''


def extract_phone(soup):
    """
    Extracts the phone number from the bytes of a web page
    :param soup: (Beautiful Soup object) corresponding Beautiful Soup
    object
    :return: (String) phone number of person or empty string if not found
    """
    # Enter your code below and remove the pass statement
    # regex for first occurrence of telephone
    regex = re.compile(r'Telephone', re.IGNORECASE)
    phone_text = soup.find_all(string=regex)
    # pattern for most variations of phone numbers
    phone_pattern = r'[(]?([0-9]{3})[)]?[-\s/.]?([0-9]{3}[-\s.]*[0-9]{4})'

    # phone_text is not empty
    if phone_text:
        # phone_text[0] is not empty string
        if phone_text[0]:
            # match phone pattern
            phone_match = re.search(phone_pattern, phone_text[0].get_text())
            # pattern is found on same line as telephone text
            if phone_match is not None:
                return phone_text[0].get_text()[phone_match.start():
                                                phone_match.end()]
            # phone number is in next section
            else:
                phone_line = phone_text[0].find_next()
                phone_match = re.search(phone_pattern, phone_line.get_text())
                if phone_match is not None:
                    return phone_line.get_text()[phone_match.start():
                                                 phone_match.end()]
                else:
                    # no number found
                    return ''
    # no number found
    return ''


def extract_education(soup):
    """
    Extracts the eduction from the bytes of a web page
    :param soup: (Beautiful Soup object) corresponding Beautiful Soup
    object
    :return: (String) eduction of person or empty string if not found
    """
    # Enter your code below and remove the pass statement
    # find all h2 headers
    h2s = soup('h2')
    # get header if it contains 'header'
    education_text = [target for target in h2s if target.get_text() ==
                      'Education']
    # print(education_text)
    if education_text:
        # get first instance of 'education'
        education_line = education_text[0].find_next()
        # next line is empty for some reason, so find next
        if education_line.get_text().strip() == '':
            education_line = education_line.find_next()
        # line is of type 'ul'
        if education_line.name == 'ul':
            education_next_line = education_line.find_next()
            education = education_next_line.get_text().replace(',', '-').\
                replace('\n', ' ').strip()
            return education
        # line is of any other type so just get the text
        else:
            education = education_line.get_text().replace(',', '-').\
                replace('\n', ' ').strip()
            # print(education)
            return education
    # found nothing
    return ''


def get_info(url):
    """
    Extract the information from a single faculty/staff web page
    :param url: (string) the address of the faculty/staff web page
    :return: a comma separated string containing: the last name,
    first name, email, phone and education
    """
    # Enter your code below and remove the pass statement
    # 1.  Call read_url to get the soup object
    # 2.  Call extract_name, extract_email, extract_phone, and
    #     extract_education to get the relevant information
    # 3.  Combine the info in one comma seperated string and return it.
    soup = read_url(url)
    # bad soup
    if soup is None:
        return None
    # extract all info and return in a tuple
    last_name, first_name = extract_name(soup)
    email = extract_email(soup)
    phone = extract_phone(soup)
    education = extract_education(soup)
    return f"{last_name},{first_name},{email},{phone},{education}\n"


def harvest(url, filename):
    """
    Harvest the information starting from the url specified and write
    that information to the file specified.
    :param url: (string)the main faculty index url
    :param filename: (string) name of the output csv file
    :return: None
    """
    # Enter your code below and remove the pass statement
    # 1.  Call get_people_links to get the relevant links from the url
    # 2.  Open the file with a context manager
    # 3.  Write the column headers to the file
    # 4.  Iterate over the links and call get_info on each one.
    # 5.  Write that information in the file
    people_links = get_people_links(url)
    with open(filename, 'w', encoding='UTF-8') as output_file:
        output_file.write('Last Name,First Name,Email,Phone Number,'
                          'Education\n')
        for link in people_links:
            people_info = get_info(link)
            # for some reason link has info but no name, so it's discarded
            if people_info is not None:
                if not people_info.startswith(","):
                    output_file.write(people_info)


def main():
    # Enter your code below and remove the pass statement
    # Check the command line argument then call the harvest function
    # more or less than 2 args
    if len(sys.argv) != 2:
        print('Error: Invalid number of arguments')
        print('Usage: scrape.py filename')
    # wrong file type
    elif not sys.argv[1].endswith('.csv'):
        print('Please specify a csv filename')
    # good args
    else:
        output_file = sys.argv[1]
        harvest(FIRST_URL, output_file)


if __name__ == '__main__':
    main()
