# Assignment 1 Part 1
# Kelly Bach

#/ics32/Assignment1Part1/Assignment1Part1/

from pathlib import Path

search = input()
searches = search.split(' ')
command = searches[0]
directory = Path(searches[1])

def get_files(dir):
    for document in dir.iterdir():
        if document.is_file():
            print(document)

def get_dir():
    for document in directory.iterdir():
        if document.is_dir():
            print(document)
            return document
 
def read_dir():
    get_files()
    get_dir()

def option_r():
    get_files(directory)
    for item in directory.iterdir():
        if item.is_dir():
            print(item)
            get_files(item)

def option_s():
    pass
def option_e():
    pass

if __name__ == '__main__':
    if command == 'L':
        if len(searches) == 3:
            option = searches[2]
            if option == '-r':
                option_r()
            elif option == 'f':
                get_files()
            elif option == '-s':
                pass
            elif option == 'e':
                pass
        else: 
            read_dir()
    elif command == 'Q':
        exit()
