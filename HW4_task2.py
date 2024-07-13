#HW4 task2
from pathlib import Path
import os

#requested function declaration
def get_cats_info(path):
    #check input path

    cats_dict = {}
    cats_dict_list = []

    file_path = Path(path)
    if file_path.exists():
        print("Provided path is correct, file exists")
    else:
        print("Provided path does not exists! Exit!")
        os._exit(-1)
    
    #open file and use "with as" to protect unclosed file 
    with open(path, "r",encoding="UTF8") as cats_file:
        #read file content line by line, strip lines to delete \n and split by comma
        while True:
            line_striped = cats_file.readline().strip()
            if not line_striped:
                break
            line_splitted = line_striped.split(',')
            print(line_splitted)

            #add cats data to dictionary
            cats_dict["id"] = line_splitted[0]
            cats_dict["name"] = line_splitted[1]
            cats_dict["age"] = line_splitted[2]
            print(cats_dict)

            #append cats dictionaries to list of dictionaries
            cats_dict_list.append(cats_dict.copy())
        
        print(cats_dict_list)
        return cats_dict_list

#test data
path = "test_cats.txt"
list2 = get_cats_info(path)
print(list2)