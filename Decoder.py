# Douglas A. Harrison | UFID: 1623-1785

'''
Declare global variables option, password, and encoded_password
 for use in the menu, storing passwords, and decoding passwords,
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


def decoding(word):
    '''
    Define decoding function to take password as arg and increment each
    value by -33. If the increment results in a value less than 0, add 10
    '''

    encoded_password = ""

    for i in range(0, len(word)):
        new_item = ((int(word[i]) - 3))
        if new_item < 0:
            new_item += 10
        encoded_password += str(new_item)

    return encoded_password

if __name__ == '__main__':
    menu()

    while option != 3:
        # Loop menu and produce appropriate output for a given menu option
        if option == 1:
            password = str(input('Please enter your password to decode: '))
            print('Your password has been decoded and stored!', '\n')
        elif option == 2:
            print('The original password is ' + str(decoding(password)) + ', and the encoded password is ' + password + '.')

        menu()

    # if option 3 is selected, program no longer returns output
    
