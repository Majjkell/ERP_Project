""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
    spaces = []
    len_of_table = len(table[0])
    for i in range(len_of_table):
        spaces.append(0)
    
    for lisst in table:
        for idx ,  lissst in enumerate(lisst):
            if len(lissst) > spaces[idx]:
                spaces[idx] = len(lissst)+1
            if len(title_list[idx]) > spaces[idx]:
                spaces[idx] = len(title_list[idx])+1

    how_many_spaces = 0

    for space in spaces:
        how_many_spaces = how_many_spaces + space

    how_many_spaces = how_many_spaces+len_of_table*2-1  
    print("/"+how_many_spaces*"-"+"\\")

    for idc, lisst in enumerate(table):
        Line_in_table = ""
        Line_in_Title_list = ""
        for idx , lissst in enumerate(lisst):
            speces_in_table = int((spaces[idx]-len(lissst)))
            spaces_in_title_list = int((spaces[idx]-len(title_list[idx])))
            space_for_nice_looking_table = 1
            if idx ==0:
                space_for_nice_looking_table=0
            if idc ==0:
                Line_in_Title_list =  Line_in_Title_list + space_for_nice_looking_table * " " + "|" + spaces_in_title_list * " " + title_list[idx]
            Line_in_table = Line_in_table + space_for_nice_looking_table * " " + "|" + speces_in_table * " " + lissst 
        if idc == 0:
            Line_in_Title_list = Line_in_Title_list +" "+"|"
            print(Line_in_Title_list)    
        Line_in_table = Line_in_table +" "+"|"
        print("|"+how_many_spaces*"-"+"|") 
        print(Line_in_table)   
    print("\\"+how_many_spaces*"-"+"/")
    


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    option_number = 1
    spaces = "    "
    print(title,":")
    for option in list_options:
        print(spaces+"("+str(option_number)+")", option)
        option_number +=1
    print(spaces+"(0)",exit_message)
        
        



def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = [input("Please enter a number: ")]

    # your code

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
