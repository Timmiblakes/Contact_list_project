# Add, Update, Delete and List contacts
# The implementation of the database written files on a notepad file is the only implementation remaining

def main():
    # Remove this dummy data and use the database (notepad) very soon.
    original_database_for_names = ["EMMA", "JENNIFER", "JOSH", "FRIDAY"]
    original_database_for_numbers = [8054564778, 7058764779, 9064789112, 5012345778]

    # Forking the database
    list_of_numbers = original_database_for_numbers.copy()
    list_of_names = original_database_for_names.copy()

    # Getting user input
    menu_feedback = input("Do you want to add, delete, update or list the numbers?\nEnter 'A' to Add a contact\n"
                          "Enter 'D' to Delete a contact\nEnter 'U' to update a contact information\n"
                          "Enter 'L' to list your contacts\n\nEnter your reply here: ")

    # Checking for what task the user wants to perform
    if (menu_feedback == 'A') or (menu_feedback == 'a'):
        adding(list_of_names, list_of_numbers)
    elif (menu_feedback == 'D') or (menu_feedback == 'd'):
        deleting(list_of_names, list_of_numbers)
    elif (menu_feedback == 'U') or (menu_feedback == 'u'):
        updating(list_of_names, list_of_numbers)
    elif (menu_feedback == 'L') or (menu_feedback == 'l'):
        listing(list_of_names, list_of_numbers)
    else:
        print("Your input is invalid")


def database(list_of_names, list_of_numbers):
    # This function merges that forked data with the actual database
    original_database_for_names = list_of_names
    original_database_for_numbers = list_of_numbers
    original_database_for_names.upper()


def adding(list_of_names, list_of_numbers):
    # The adding operation
    contact_name = input("Enter the name of the contact you would like to store: ")
    contact_number = input("Enter the phone number of the contact you would like to store: ")
    all_caps_names = contact_name.upper()
    list_of_names.append(all_caps_names)
    current_number = int(contact_number)
    list_of_numbers.append(current_number)
    database(list_of_names, list_of_numbers)


def deleting(list_of_names, list_of_numbers):
    # The deleting operation
    name = input("Enter the name of the person you would like to delete from your contact list: ")
    contact_name = name.upper()
    if contact_name in list_of_names:
        position = list_of_names.index(contact_name)
        list_of_names.remove(list_of_names[position])
        list_of_numbers.remove(list_of_numbers[position])
        database(list_of_names, list_of_numbers)
    else:
        print("Invalid name")


def updating(list_of_names, list_of_numbers):
    # The updating operation
    # Asking whether the user wants to update the name or phone number of the contact or both.
    signal = False
    while signal is False:
        response = input("What would you like to update -  the name or the number of the contact?\nEnter in 'N'"
                         "for name or 'P' for phone number: ")
        if (response == 'N') or (response == 'n'):
            contact_name = input("Enter the name of the contact you would like to update: ")
            upper_contact_name = contact_name.upper()
            if upper_contact_name in list_of_names:
                position = list_of_names.index(upper_contact_name)
                name = input("Please enter the replacement name: ")
                updated_name = name.upper()
                list_of_names.remove(list_of_names[position])
                list_of_names.insert(position, updated_name)
                signal = True
            else:
                print("Name not found!!")
        elif (response == 'p') or (response == 'P'):
            contact_number = input("Enter the number of the contact you would like to update: ")
            int_contact_number = int(contact_number)
            if int_contact_number in list_of_numbers:
                position = list_of_numbers.index(int_contact_number)
                updated_number = input("Please enter the replacement number: ")
                list_of_numbers.remove(list_of_numbers[position])
                list_of_numbers.insert(position, updated_number)
                signal = True
            else:
                print("Number not found!!")
        else:
            print("Invalid input!!")
    database(list_of_names, list_of_numbers)


def listing(list_of_names, list_of_numbers):
    # The listing operation
    length_of_database = len(list_of_names)
    for i in range(0, length_of_database):
        print(list_of_names[i], "\n", list_of_numbers[i], "\n", sep="")


main()
