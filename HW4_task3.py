#HW4 task3
from pathlib import Path
from colorama import Fore, Back, Style
import sys
import os

#function to be called for recursive directory print
def print_directory(dir_path, level = 0):
    #loop to iteratively go over directories and if can go deeper, call function again
    for item in dir_path.iterdir():
        if item.is_dir():
            print(" " * level * 4 + Fore.BLUE + str(item))
            print_directory(item, level + 1)
        else:
            print(" " * level * 4 + Fore.GREEN + str(item))
    
    Style.RESET_ALL

#main script function
def main():
    #check the amount of provided arguments
    if len(sys.argv) > 2:
        print("Too many arguments, only path is expected")
        os._exit(-1)

    directory_path = Path(sys.argv[1])
    if  directory_path.exists():
        print("Provided path is correct, file exists")
    else:
        print("Provided path does not exists! Exit!")
        os._exit(-1)

    print_directory(directory_path) 
    

#check if script called from terminal or imported to other module
if __name__ == "__main__":
    main()





