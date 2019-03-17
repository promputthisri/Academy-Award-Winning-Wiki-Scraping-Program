#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib.request as ureq
import sys

# URL
URL = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'

# access page html
opened_page = ureq.urlopen(URL)
page_html = opened_page.read()
opened_page.close()

# parse page htmland find all elements belonging to "tr" tag
soup = BeautifulSoup(page_html)
movieRow = soup.findAll("tr")

# aquire movie title and year in a dictionary call "titleYear"
titleYear = {}
print("Retrieving title and year...")
for row in movieRow:
    aLine = row.findAll("a")
    if aLine and len(aLine) == 2:
        name = aLine[0].text
        year = aLine[1].text
        try:
            if titleYear[year]:
                titleYear[year].append(name)
        except Exception as e:
            titleYear[year] = []
            titleYear[year].append(name)

# usful function
def valid_year(year):
    i == 1964
    while i <= 2019:
        if (year == i):
            return True
        i += 1
    print("not a valid year-input")
    return False;

def bestMovie(year):
    return titleYear[year][0]

def getNominees(year):
    return titleYear[year]

def findMovie(movie):
    for year in titleYear:
        films = titleYear[year]
        i = 0
        for film in films:
            if film == movie and i == 0:
                return year, True
            elif film == movie:
                return year, False
            i += 1
    return 0

def helpPro():
    print("1) input 'winner of year' to find the winner of that year.")
    print("2) input 'nominees of year' to find nominee of that year.")
    print("3) input 'year of movie title' to find year that the movie won.")
    print("4) input 'help' for help.")
    print("5) input 'exit' to exit.")
# user interface

print("Welcome to Academy Award film Program. Please do as follow.")
helpPro()
while True:
    command = input("input: ")
    listCommand = command.split(' of ')
    function = listCommand[0]
    if (function == 'help'):
        helpPro()
    elif (function == "exit"):
        sys.exit()
    elif (function == "winner"):
        year = listCommand[1]
        print(bestMovie(year))
    elif (function == "nominees"):
        year = listCommand[1]
        movieList = getNominees(year)
        for movie in movieList:
            print(movie)
    elif (function == "year"):
        tupe = findMovie(listCommand[1])
        if tupe[1]:
            print(tupe[0])
        else:
            print(listComand[1] + " is the nominee for " + tube[0] + " oscar.")
    elif (function == "winner" or function == "nominees" or function == "year"):
        print("Such movie do not win anything in the past.")
    else:
        print("Your comand might be in wrong format, please try again.")