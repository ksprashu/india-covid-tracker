# parse the MOHFW website and retrieve the statewise covid data
#!/usr/bin/env python

# import beautiful soup and requests
from bs4 import BeautifulSoup
import requests

# constant: url of website 
URL = "http://www.mohfw.gov.in/"

# constant: classname for table element
TABLE_CLASS_NAME = "statetable"
TABLE_DIV = "data-table"

# function to get the contents in a table element identified by a classname
def get_table_rows(soup):
    # find the table element with the specified class name
    # table = soup.find("table", class_=TABLE_CLASS_NAME)

    # div_element = soup.find("div", class_=TABLE_DIV)
    # table_body = div_element.find("tbody")

    # get elements by classname
    
    # get all the rows in the table
    table_body = soup.find("tbody")    
    rows = table_body.find_all("tr")

    # return a list of rows
    return rows


# function to get contents of website and return a soup object
def get_soup(url):
    # get the html content of the website
    response = requests.get(url)

    # parse the html content
    soup = BeautifulSoup(response.content, "lxml")

    # return the soup object
    return soup


# invoke main function
def main():

    soup = get_soup(URL)
    rows = get_table_rows(soup)
    print(rows)


# call the main function
if __name__ == "__main__":
    main()

