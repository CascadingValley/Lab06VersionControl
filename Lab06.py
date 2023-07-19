# Douglas A. Harrison | UFID: 1623-1785

'''
Declare global variables option, password, and encoded_password
 for use in the menu, storing passwords, and encoding passwords,
respectively.
'''

option = 0

global password
password = ""

global encoded_password
encoded_password = ""


def menu():
    #  Define menu function to display menu options and request input
    print('Menu', '--------', '1. Encode', '2. Decode', '3. Quit',
          sep = '\n', end = '')

    print('\n')

    global option
    option = int(input('Please enter an option: '))


def encoding(word):
    '''
    Define encoding function to take password as arg and increment each
    value by 3. If the increment results in a value greater than 10, subtract 10
    '''

    encoded_password = ""

    for i in range(0, len(word)):
        new_item = ((int(word[i]) + 3))
        if new_item >= 10:
            new_item -= 10
        encoded_password += str(new_item)

    return encoded_password

if __name__ == '__main__':
    menu()

    while option != 3:
        # Loop menu and produce appropriate output for a given menu option
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!', '\n')
        elif option == 2:
            print('The encoded password is ' + str(encoding(password)) + ', and the original password is ' + password + '.')

        menu()

    # if option 3 is selected, program no longer returns output
    