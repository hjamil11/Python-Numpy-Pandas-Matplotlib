####################################################################
##   Author:         Hamad Ahmed                                  ##
##   Major:          Computer Science                             ##
##   Creation Date:  February 11, 2022                            ##
##   Due Date:       Febuary 18, 2022                             ##
##   Course:         CSC_223_010                                  ##
##   Professor Name: Earl                                         ##
##   Assignment:     #2                                           ##
##   Filename:       hw1_payroll.py                               ##
##   Purpose:        This goal of the program is to compute a     ##
##                   sale statistics for each of it's various     ##
##                   departments.                                 ##
####################################################################



def get_data(f_name):
  '''
  Function Name: get_data
  Description:   Takes a string file. The reads the standard sales and 
                 a list of lists from the file, and turn it into float
  Parameters:    string f_name: file name - input
  Return Value:  List standardList
                 List float_Lists  
  '''
  
  # Opens the file and closes it after it's scope
  with open(f_name) as f:
    # Reads the first line from the file, and stores it in standardList
    standardList = f.readline()

    # Calls the string_to_float_list() to covert standardList to a float list
    standardList = string_to_float_list(standardList)

    # Then, reads the rest of the file and store it in sales_Lists
    sales_Lists = f.readlines()

    # Declares a float_lists list
    float_Lists = []

    # This for loop turns the sales_Lists string data into a float 2d lists
    for row in sales_Lists:
      float_Lists.append(string_to_float_list(row)) 
    
  return(standardList, float_Lists)



def process_data(floatLists, standardList):
    '''
    Function Name: process_data
    Description:   Takes the floatLists and standardList and turns it in
                   a list of dictionary. In the list of dictionary computes the 
                   department number, average, above, below, and satisfaction.
    Parameters:    List floatLists: list of lists of float - input
                   List standardLists: standard sales list - input
    Return Value:  List - list of dictionary
    '''

    # Declares a list_Of_Dictionaries list()
    list_Of_Dictionaries = []

    # Declares a counter variable for Department numbers
    dept_Number = 1

    # Computes the sales' "department","average","above","below","Performance"
    # Then, turn this data into a dictionary
    # At last, turns the dictionary into a list of dictionaries
    for department in floatLists:
        # Computes the average of department sales
        average = round(sum(department)/len(department), 1)

        # Compares the sales
        # And computes the sales that are below or above the standard sales
        above, below = sales_cmp(standardList, department)

        # Declares a string variable satisfaction
        satisfaction = ''
        
        # If the sales are below than 5 or equal from the standard sales:  
        if below <= 5: 
          # Then, the satisfaction is satisfied
          satisfaction = 'satisfied'
        else:
          # Otherwise, the satisfaction is unsatisfied
          satisfaction = 'unsatisfied'

        # Forms the data computed into a dictionary
        data_dict = {
            "Department": dept_Number,
            "Average": average,
            "Above": above,
            "Below": below,
            "Performance": satisfaction
        }
        
        # Turns the dictionary into a list of dictionary
        list_Of_Dictionaries.append(data_dict)

        # Increment the department number per department
        dept_Number += 1 
    
    return(list_Of_Dictionaries)



def write_to_file(listOfDictionaries):
    '''
    Function Name: write_to_file
    Description:   Takes the list of dictionaries data and writes it to
                   the file named 'out.dat'
    Parameters:    list listOfDictionaries: list of dictionaries - input
    Return Value:  None
    '''

    # Declares an empty string 'stringList' and a counter 'i'
    stringList = ''
    i = 0

    # This for loop takes the keys from the list of dictionaries and 
    # assigns them to stringList. Moreover, it then takes data from
    # the list of dictionaries and appends it to string list
    for dict in listOfDictionaries:
        if(i==0):
            stringList = ",".join(dict.keys()) + "\n"
            i+=1

        # 
        stringList += ",".join(dictionary_to_list(dict)) + "\n"
    
    # Opens a new file, writes the stringList data into it, and closes the file
    with open("out.dat",'w') as newFile:
      newFile.write(stringList)



def string_to_float_list(string):
    '''
    Function Name: string_to_float_list
    Description:   Turns the string list to a float list
    Parameters:    List string: string list - input
    Return Value:  List floatList
    '''

    # Assigns the splitted str by space to lists
    lists = string.split(" ")

    # Declares an empty list 'floatList'
    floatList = []

    # Turns the data in lists to float and appends it to floatList
    for item in lists:
        floatList.append(float(item))
    return(floatList)



def dictionary_to_list(dictionary):
  '''
  Function Name: dictionary_to_list
  Description:   Takes a dictionary and turns it into a list
  Parameters:    dict dictionary: a dictionary - input
  Return Value:  List string_List
  '''

  # Declares am empty list 'string_List'
  string_List = []

  # This for loop takes the data in a dictionary and appends it to a string list
  for elt in dictionary:
      string_List.append(str(dictionary[elt]))
  return string_List  


def sales_cmp(standard,department):
  '''
  Function Name: sales_cmp
  Description:   Compares the monthly sales with standard sales, and
                 determines if it is above or below 
  Parameters:    List standard: standard sales list - input
                 List department: department numbers - input
  Return Value:  int above
                 int below
  '''

  # Declares int variables above and below, and set them equal to 0
  above = 0
  below = 0

  # This for loops compares monthly sales to the standard sales
  for elt in range(len(standard)):
    # Checks if the monthly sales are greater, equal, or below the standard
    # sales
    if (department[elt] >= standard[elt]):
      above += 1
    else:
      below += 1

  return above, below
  

def main():
  '''
  Function Name: main
  Description:   Prompts the user for the file name, and calls the other
                 functions in an appropriate
  Parameters:    None
  Return Value:  None
  '''

  # Prompts the user for a filename
  fileName = str(input("Enter the file name: "))

  # Call the other functions in an appropriate order and arguments 
  std_List, sales_List =  get_data(fileName)
  list_of_Dict = process_data(sales_List, std_List)
  write_to_file(list_of_Dict)

# Calls the main function 
main()