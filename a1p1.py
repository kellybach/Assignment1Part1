# Assignment 1 Part 1
# Kelly Bach

#/ics32/Assignment1Part1/Assignment1Part1/

from pathlib import Path

search = input()
searches = search.split(' ')
command = searches[0]
directory = Path(searches[1])

def get_files():
    for document in directory.iterdir():
        if document.is_file():
            print(document)

def get_dir():
    for document in directory.iterdir():
        if document.is_dir():
            print(document)
 
def read_dir():
    get_files()
    get_dir()

if __name__ == '__main__':
    if command == 'L':
        read_dir()
    elif command == 'Q':
        exit()
