#HW4 task1

#import Path to check if provided file path is correct and file exists
from pathlib import Path
import os

#function will read data from file and calculate total and avarage salary
def total_salary(path):
    #check path first
    file_path = Path(path)
    if file_path.exists():
        print("Provided path is correct, file exists")
    else:
        print("Provided path does not exists! Exit!")
        os._exit(-1)


    splitted_data = []
    salary_from_file = []

    #open file and use "with as" to protect unclosed file 
    with open(path, "r",encoding="UTF8") as salary_file:
        #read file content line by line, strip lines to delete \n and split by comma
        while True:
            line_striped = salary_file.readline().strip()
            if not line_striped:
                break
            line_splitted = line_striped.split(',')
            splitted_data.extend(line_splitted)
        print(splitted_data)

    #create new list with integer salaries only    
    salary_list = [int(x) for x in splitted_data if x.isdigit()]
    print(salary_list)

    #get number of salary units in list and total 
    number = len(salary_list)
    total_sum = sum(salary_list)

    #calculate average salary    
    avarege_salary = total_sum / number

    return total_sum, avarege_salary  

#test data
path_to_file = "test_data.txt" 
total, average = total_salary(path_to_file)
print(f"\ntotal is {total}, average is {average}")
        
path_to_file = "test_data1.txt" 
total, average = total_salary(path_to_file)
print(f"\ntotal is {total}, average is {average}")
 



