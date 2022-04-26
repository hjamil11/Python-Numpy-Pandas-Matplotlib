#######################################################################################
## Author:              Hamad Ahmed                                                  ##
## Major:               Computer Science                                             ##
## Creation Date:       February 25, 2022                                            ##
## Due Date:            March 4, 2022                                                ##
## Course:              CSC 223                                                      ##
## Professor Name:      Earl                                                         ##
## Assignment:          #3                                                           ##
## Filename:            main.py                                                      ##
## Purpose:             This program will take a csv file named "netflix_titles.csv" ##
##                      Then, it will read show id, title, director, country,        ##
##                      date added and duration of all TV shows in the file.         ##
##                      Furthermore, it will sort the data by duration in            ##
##                      descending order. Finally, dumps the sorted data in a        ##
##                      json file.                                                   ##
#######################################################################################

# Imports the 'csv' and 'json' libraries
import csv
import json

#######################################################################################
def get_data():
    '''
    Function Name: get_data
    Description:   Takes a csv file. Then reads the show id, title, director, country, 
                   date added, and duration for all the TV Shows. Morover, stores the 
                   specific TV shows data into each individual list
    Parameters:    none
    Return Value:  List show_id - every TV show's show id
                   List title - every TV show's title
                   List director - every TV show's director
                   List country - every TV show's country 
                   List date_added - every TV show's date added
                   List duration - every TV show's duration
    '''

    # Opens the 'netflix_titles.csv' file, as csv_file, and changes the default encoding
    # to 'utf-8' to read the special characters in the csv file. Moreover, the file closes
    # after the statements in its scope.
    with open('netflix_titles.csv', encoding = 'utf-8') as csv_file:
        # 'csv_file_reader' reads the 'csv_file'
        csv_file_reader = csv.reader(csv_file)

        # Creates lists to store every TV show's show id, title, director, country, date added, 
        # and duration.
        show_id = []
        title = []
        director = []
        country = []
        date_added = []
        duration = []

        # Moves the position to the second line in the csv_file, skipping the heading row.
        next(csv_file_reader)

        # Retrieves the appropriate information of every TV show and appends it to its
        # appropriate list.
        for line in csv_file_reader:
            if line[1] == 'TV Show':
                show_id.append(line[0])
                title.append(line[2])
                director.append(line[3])
                country.append(line[5])
                date_added.append(line[6])
                duration.append(line[9])

    # Returns the show id, title, director, country, date added and duration of every TV show.
    return show_id, title, director, country, date_added, duration

#######################################################################################

def process_data(show_id, title, director, country, date_added, duration):
    '''
    Function Name: process_data
    Description:   Takes the specific data of all TV Shows. Then,
                   calls the sort_data() function to sort the data 
                   descendingly by each show's duration. Furthermore,
                   turns the data into a dictionary of lists of specific
                   data. 
    Parameters:    List show_id - every TV show's show id
                   List title - every TV show's title
                   List director - every TV show's director
                   List country - every TV show's country 
                   List date_added - every TV show's date added
                   List duration - every TV show's duration
    Return Value:  List of dictionaries data_dict: TV shows information dictionaries
    '''

    # Calls the helper function 'sort_data' that sorts the TV shows information
    # in descending order by its duration or the number of seasons. 
    sort_data(show_id, title, director, country, date_added, duration)

    # Creates a list 'data_dict' that will store TV shows information as dictionaries
    data_dict = []

    # This for loop appends the TV shows information into 'data_dict' a list of 
    # dictionaries 
    for idx in range(len(duration)):
        data_dict.append(
            {
            "Show_ID": show_id[idx],
            "Title": title[idx],
            "Director": director[idx],
            "Country": country[idx],
            "Date_Added": date_added[idx],
            "Duration": duration[idx]
            }
        )

    # Returns the 'data_dict', a list of dictionaries
    return data_dict

#######################################################################################

def write_to_file(data_dict):
    '''
    Function Name: write_to_file
    Description:   Takes the list of dictionaries data and dumps it to
                   a json file named 'output.json'
    Parameters:    List of Dictionaries data_dict: TV shows information dictionaries
    Return Value:  None
    '''

    # Opens or creates a json output File 'output.json' as outFile, and dumps 'data_dict',
    # the list of dictionaries
    with open('output.json', 'w') as outFile:
        json.dump(data_dict, outFile, indent = 4)

#######################################################################################

def sort_data(show_id, title, director, country, date_added, duration):
    '''
    Function Name: sort_data
    Description:   Takes the TV shows information lists and sort them in 
                   descending order
    Parameters:    List show_id - every TV show's show id
                   List title - every TV show's title
                   List director - every TV show's director
                   List country - every TV show's country 
                   List date_added - every TV show's date added
                   List duration - every TV show's duration
    Return Value:  None
    '''

    # This nested for loop sorts the parameter lists in descending order
    # by it's duration
    for n in range(len(duration)):
        for k in range(n + 1, len(duration)):
            if duration[n] < duration[k]:
                duration[n], duration[k] = duration[k], duration[n]
                show_id[n], show_id[k] =  show_id[k], show_id[n]
                title[n], title[k] = title[k], title[n]
                director[n], director[k] = director[k], director[n]
                country[n], country[k] = country[k], country[n]
                date_added[n], date_added[k] = date_added[k], date_added[n]

#######################################################################################

def main():
    '''
    Function Name: main
    Description:   Calls the other functions in an appropriate order
    Parameters:    None
    Return Value:  None
    '''

    # Stores the return value of 'get_data' function in their appropriate lists
    show_id, title, director, country, date_added, duration = get_data()

    # Stores the list of dictionaries returned by 'process_data', that takes in 'get_data' 
    # function return values, in 'data_dict'
    data_dict = process_data(show_id, title, director, country, date_added, duration)

    # Lastly, calls the 'write_to_file' function that takes in 'data_dict', and writes to
    # a json file
    write_to_file(data_dict)

# Calls the main function
main()