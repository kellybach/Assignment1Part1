# Assignment 1 Part 1
# Kelly Bach
# 18576745
# kbach3@uci.edu

from pathlib import Path

search = input()
searches = search.split(' ')
command = searches[0]
directory = Path(searches[1])

def get_files(dir):
    for document in dir.iterdir():
        if document.is_file():
            print(document)

def get_dir(dir):
    for document in dir.iterdir():
        if document.is_dir():
            print(document)
 
def read_dir():
    get_files(directory)
    get_dir(directory)

def option_r(dir):
    for item in dir.iterdir():
        if item.is_dir():
            print(item)
            get_files(item)
            option_r(item)
                

def option_s():
    pass

def option_e():
    e = sorted(directory.glob(f'*.{searches[3]}'))
    for item in e:
        print(item)
def option_re():
    e = sorted(directory.glob(f'**/*.{searches[4]}'))
    for item in e:
        print(item)


if __name__ == '__main__':
    if command == 'L':
        if len(searches) == 3:
            option = searches[2]
            if option == '-r':
                get_files(directory)
                option_r(directory)
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
                get_files(directory)
                option_r(directory)

        if len(searches) == 5: 
            option = searches[3]
            if option == '-s':
                get_files(directory)
                option_r(directory)
                option_s()
            elif option == '-e':
                option_re()
    elif command == 'Q':
        exit()
