# ----------------------------------------------------------------------
# Name:        scrape.py
# Purpose:     Homework 8 - practice web scraping
# Author(s): Shu Sian (Jessie) Lyu, An Tran
# Date: 04/20/2023
# ----------------------------------------------------------------------
"""
Implementation of web scraping

This program will take in a name of the csv file as a command line argument
and start by opening and reading the SJSU faculty index page at
https://sjsu.edu/people/. It will then proceed to extract information about
each faculty or staff and save the information in the csv file specified.
"""

import urllib.request
import urllib.error
import bs4
import re
import sys
import os

BASE_URL = "https://sjsu.edu/people/"


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
    except Exception as other_err:  # safer on the web
        print(f'Other error with url: {url}\n{other_err}')
    else:
        soup = bs4.BeautifulSoup(url_bytes, 'html.parser')
        return soup


def get_people_links(url):
    """
    Read the given url and return the relevant referenced links.
    :param url:(string) - the address of the faculty index page
    :return: (list of strings) - the relevant people links
    """
    soup = read_url(url)('a')
    pattern = r'/people/[a-z]+'  # pattern for relevant referenced links

    result = [urllib.parse.urljoin(BASE_URL, each_anchor.get('href', None))
              for each_anchor in soup if re.match(pattern, each_anchor.get
              ('href', None))]

    return result


def extract_name(soup):
    """
    Extract the first and last name from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a tuple of strings representing the first and last names
    """
    h1 = soup('h1')
    # check if h1 is found in the web
    if h1:
        full_name = h1[0].get_text()
        # deal with the different formats of full name
        if ',' in full_name:
            return full_name.split(', ')[1].strip(), full_name.split(', ')[
                0].strip()
        else:
            if len(full_name.split()) > 2:
                return full_name.split()[0].strip(), full_name.split()[
                    -1].strip()
            if len(full_name.split()) == 2:
                return full_name.split()[0].strip(), full_name.split()[
                    1].strip()


def extract_email(soup):
    """
    Extract the email from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a string that representing the email
    """
    # compile regex for emails
    regex = re.compile(r'@\S+(.edu|.com|.org)', re.IGNORECASE)
    all_emails = soup.find_all(string=regex)
    # check if email is found in the page
    if all_emails:
        return all_emails[0].strip()


def extract_phone(soup):
    """
    Extract the phone number from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a string that representing the phone number
    """
    # first find the element of Telephone
    regex = re.compile(r'Telephone', re.IGNORECASE)
    phone_text = soup.find_all(string=regex)
    # pattern for phone numbers
    pattern = r'([+]?1?[\s]?[\(]?[0-9]{3}[\)]?[-./]?[\s]?[0-9]{3}[\s.-]*[' \
              r'0-9]{4})'

    if phone_text:
        phone = phone_text[0].find_next().get_text().split(":")
        if phone:
            if re.match(pattern, phone[-1].strip()):
                return re.match(pattern, phone[-1].strip()).group()


def extract_education(soup):
    """
    Extract the education from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a string that representing the education
    """
    # first find the element of Education
    result = soup('h2')
    for each in result:
        if each.get_text() == "Education":
            next_element = each.find_next()
            if next_element.get_text().strip() == '':
                next_element = next_element.find_next()
            if next_element.name == 'ul':
                return next_element.find_next().get_text().\
                    replace(",", "-").replace("\n", " ").strip()
            else:
                return next_element.get_text().replace(',', '-').\
                    replace("\n", " ").strip()


def get_info(url):
    """
    Extract the information from a single faculty/staff web page
    :param url: (string) the address of the faculty/staff web page
    :return: a comma separated string containing: the last name,
    first name, email, phone and education
    """
    # Call read_url to get the soup object
    soup = read_url(url)

    # check if soup and required names are found in the page
    if soup and extract_name(soup):
        first_name, last_name = extract_name(soup)
        email = extract_email(soup)
        phone = extract_phone(soup)
        education = extract_education(soup)
        result = [last_name, first_name, email, phone, education]

        # replace None with empty string
        for i in range(len(result)):
            if not result[i]:
                result[i] = ""

        # Combine the info in one comma seperated string and return it.
        return ','.join(result)


def harvest(url, filename):
    """
    Harvest the information starting from the url specified and write
    that information to the file specified.
    :param url: (string)the main faculty index url
    :param filename: (string) name of the output csv file
    :return: None
    """

    # Call get_people_links to get the relevant links from the url
    people_links = get_people_links(url)
    # Open the file with a context manager and write the headers of the file
    with open(filename, "w", encoding='UTF-8') as output_file:
        output_file.write(f"Last Name,First Name,Email,Phone Number,"
                          f"Education\n")
        # Iterate over the links and call get_info on each one
        for link in people_links:
            # check if the info is return successfully
            if get_info(link):
                # Write that information in the file
                output_file.write(get_info(link) + '\n')


def main():
    # Check the command line argument then call the harvest function
    if len(sys.argv) != 2:
        print('Error: Invalid number of arguments')
        print('Usage: scrape.py filename')
    else:
        filename = sys.argv[1]
        ext = os.path.splitext(filename)[1]
        if ext != ".csv":
            print('Please specify a csv filename')
            return
        harvest(BASE_URL, filename)


if __name__ == '__main__':
    main()
