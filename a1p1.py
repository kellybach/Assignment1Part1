# Assignment 1 Part 1
# Kelly Bach

# L /ics32/Assignment1Part1/Assignment1Part1/ -r -s
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
    get_files(directory)
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
            elif option == '-f':
                get_files(directory)
            else: 
                read_dir()
        if len(searches) == 4:
            option = searches[2]
            if option == '-s':
                option_s()
            elif option == '-e':
                option_e()
            else:
                option_r()
                get_files(directory)
        if len(searches) == 5: 
            option = searches[3]
            if option == '-s':
                option_r()
                option_s()
            elif option == '-e':
                option_r()
                option_e()
    elif command == 'Q':
        exit()
