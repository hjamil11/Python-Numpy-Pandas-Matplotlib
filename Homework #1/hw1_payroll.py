####################################################################
##   Author:         Hamad Ahmed                                  ##
##   Major:          Computer Science                             ##
##   Creation Date:  January 31, 2022                             ##
##   Due Date:       Febuary 11, 2022                             ##
##   Course:         CSC_223_010                                  ##
##   Professor Name: Professor Earl                               ##
##   Assignment:     #1                                           ##
##   Filename:       hw1_payroll.py                               ##
##   Purpose:        This program will accept an employee's name, ##             
##                   hours for each of 5 days, and keep accepting ##        
##                   this information until the user types done.  ##           
##                   Then, computer each employee's gross pay,    ##              
##                   total withholding amount and net pay.        ##         
##                   Finally, display each employee's information.## 
####################################################################

# Imports the 'sys' header library
import sys

# Declares the necessary variables
stateTax = 0.0307
fica = 0.0886

option = False

# This while loop keeps accepting the data until the user types 'done'
while not option:
    # Declare the necessary variables
    grossPay = 0.0
    withHolding = 0.0
    netPay = 0.0
    total_hours = 0

    # Prompts the user for employee
    name = str(input("Enter employee name: "))
    print('\n')

    # Validates if the user types 'done', then the program terminates
    if (name.lower() == "done"):
        option = True
        break

    # Prompts the user for their wage and validate the data
    payRate = float(input("Enter your wage: "))
    print('\n')
    if (payRate < 0.0):
        print("Invalid entry, please run the program again and enter the valid wage")
        break
    
    # Prompts the user for their hours worked for 5 days and validate the data
    for i in range(5):
        hoursWorked = int(input("Enter the hours worked on day " + str(i + 1) + ": "))
        if (hoursWorked < 0 or hoursWorked > 24):
            print("Invalid entry, please run the program again and enter the valid hours")
            sys.exit()
        total_hours += hoursWorked
        # Computes the user's gross pay
        grossPay = grossPay + (payRate * hoursWorked)

    # Computes the total withholding amount based on the user's gross pay
    if grossPay < 5000.0:
        withHolding = grossPay * (stateTax + fica + 0.15)
    else:
        withHolding = grossPay * (stateTax + fica + 0.25)

    # Computes the user's net pay
    netPay = grossPay - withHolding

    # Displays the employee information
    print('\n')
    print("Employee Name:", name)
    print("Total Hours Worked: ", '{:d}'.format(total_hours))
    print("Gross Pay: $", '{:6.2f}'.format(grossPay))
    print("Total Withholding Amount: $", '{:4.2f}'.format(withHolding))
    print("Net Pay: $", '{:4.2f}'.format(netPay))
    print('\n')

    # Prompts the user if they want to continue or quit the program 
    #choice = str(input("Please enter any key to continue and 'done' to quit the program: "))
    #print('\n')

    # Check to see if the user's choice is True, then terminate the program.
    #if (choice.lower() == "done"):
    #   option = True