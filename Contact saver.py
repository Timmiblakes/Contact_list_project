# Add, Update, Delete and List contacts

def main():
    # Creating a list and getting the data from a .txt file in the python folder.
    database_names = []
    database_numbers = []
    original_database_for_names, original_database_for_numbers = get_info_from_database(database_names, database_numbers
                                                                                        )

    # Forking the database to a temporary list so the original list doesn't get messed up during the process of editing
    list_of_numbers = original_database_for_numbers.copy()
    list_of_names = original_database_for_names.copy()

    # Listing the contacts
    listing(list_of_names, list_of_numbers)

    # Getting user input for what action to perform
    menu_feedback = input("Do you want to add, delete, update or list the numbers?\nEnter 'A' to Add a contact\n"
                          "Enter 'D' to Delete a contact\nEnter 'U' to update a contact information\n"
                          "Enter 'L' to list your contacts\n\nEnter your reply here: ")

    # Checking for what action the user wants to perform
    if (menu_feedback == 'A') or (menu_feedback == 'a'):
        adding(list_of_names, list_of_numbers)
    elif (menu_feedback == 'D') or (menu_feedback == 'd'):
        deleting(list_of_names, list_of_numbers)
    elif (menu_feedback == 'U') or (menu_feedback == 'u'):
        updating(list_of_names, list_of_numbers)
    elif (menu_feedback == 'L') or (menu_feedback == 'l'):
        listing(list_of_names, list_of_numbers)
    else:
        print("\nYour input is invalid\n")


def database(list_of_names, list_of_numbers):
    # Takes the edited list that was copied earlier on, clears the .txt file, and then replaces it with the edited one
    with open('Name Database.txt', 'w') as names:
        names.truncate(0)
        for item in list_of_names:
            names.write("%s\n" % item)
    with open('Phone Number Database.txt', 'w') as numbers:
        numbers.truncate(0)
        for item in list_of_numbers:
            numbers.write("%s\n" % item)


def get_info_from_database(database_for_names, database_for_numbers):
    # This function is called upon to get the names and numbers from two .txt files (Name Database,
    # Phone Number Database) and then add it to a list, and then the list is returned.
    with open('Name Database.txt', 'r') as names:
        for line in names:
            last_character = line[:-1]
            database_for_names.append(last_character)
    with open('Phone Number Database.txt', 'r') as numbers:
        for a in numbers:
            last_character_line = a[:-1]
            database_for_numbers.append(last_character_line)
    return database_for_names, database_for_numbers


def adding(list_of_names, list_of_numbers):
    # This function gets the name and number to be added and then sends it to the database function
    contact_name = input("Enter the name of the contact you would like to store: ")
    contact_number = input("Enter the phone number of the contact you would like to store: ")
    list_of_names.append(contact_name)
    current_number = int(contact_number)
    list_of_numbers.append(current_number)
    database(list_of_names, list_of_numbers)


def deleting(list_of_names, list_of_numbers):
    # This deletes contacts based on the name provided; if not available then it asks for input again
    signal = False
    while signal is False:
        contact_name = input("Pleas enter the full name of the person you would like to delete from your contact list: "
                             )
        temp_name = contact_name.upper()
        for elements in list_of_names:
            placeholder = elements.upper()
            if temp_name == placeholder:
                position = list_of_names.index(elements)
                list_of_names.remove(list_of_names[position])
                list_of_numbers.remove(list_of_numbers[position])
                signal = True
            else:
                pass
    database(list_of_names, list_of_numbers)


def updating(list_of_names, list_of_numbers):
    # This function updates the names of users in the forked list and then sends it to the database
    # It can change just the name or phone number at a time
    signal = False
    while signal is False:
        response = input("What would you like to update -  the name or the number of the contact?\nEnter in 'N'"
                         "for name or 'P' for phone number: ")
        if (response == 'N') or (response == 'n'):
            contact_name = input("Enter the full name of the contact you would like to update: ")
            temp_name = contact_name.upper()
            for elements in list_of_names:
                placeholder = elements.upper()
                if temp_name == placeholder:
                    position = list_of_names.index(elements)
                    name = input("Please enter the replacement name in full: ")
                    list_of_names.remove(list_of_names[position])
                    list_of_names.insert(position, name)
                    signal = True
                else:
                    pass
            print("\nThe name given is not part of our database!!\n")

        elif (response == 'p') or (response == 'P'):
            contact_number = input("Enter the number of the contact you would like to update: ")
            if contact_number in list_of_numbers:
                position = list_of_numbers.index(contact_number)
                updated_number = input("Please enter the replacement number: ")
                list_of_numbers.remove(list_of_numbers[position])
                list_of_numbers.insert(position, updated_number)
                signal = True
            else:
                print("Number not found!!")
        else:
            print("\nInvalid input!!\n")
    database(list_of_names, list_of_numbers)


def listing(list_of_names, list_of_numbers):
    # This operation just lists the names and accompanying currently in the .txt file
    length_of_database = len(list_of_names)
    for i in range(0, length_of_database):
        print(list_of_names[i], "\n", list_of_numbers[i], "\n", sep="")


main()
