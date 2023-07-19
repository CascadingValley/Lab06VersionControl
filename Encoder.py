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

def main():
    menu()
    while option != 3:
        # Loop menu and produce appropriate output for a given menu option
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!', '\n')
            encoding(password)
        elif option == 2:
            decode(encoded_password)
            print('The encoded password is ' + str(encoded_password) + ', and the original password is ' + res + '.')

        menu()

    # if option 3 is selected, program no longer returns output

encoded_password = ""
res = []

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

    global encoded_password

    for i in range(0, len(word)):
        new_item = ((int(word[i]) + 3))
        if new_item >= 10:
            new_item -= 10
        encoded_password += str(new_item)

    return encoded_password

# Decodes encoded password back into its original form
def decode(encoded_password):
    global res
    result = []

    # converts encoded_password into a string list
    x = list(str(encoded_password))
    # print(x)
    # Extends variable list result with each number in num with -3. If a number in num is 0, 1, or 2 it will return 7, 8, or 9 respectively
    try:
        for char in str(encoded_password):
            if char == '2':
                result.extend([9])
            elif char == '1':
                result.extend([8])
            elif char == '0':
                result.extend([7])
            else:
                result.extend([int(char) - 3])

    except IndexError:
        pass
    # converts list back to string to print results
    result = '[%s]' % ', '.join(map(str, result))
    result = str(result)
    result = result.replace(', ', '')
    result = result.replace('[', '')
    result = result.replace(']', '')
    result = result.replace("'", '')
    res = result
    # print(res)
    return res, encoded_password


if __name__ == '__main__':
    main()
    
