import sys


def line():
    print('-----------------------------------------------------------')


def phonenumber_input():
    print('International: (COUNTRY_CODE)(10_DIGIT_PHONE_NUMBER)')
    print('or')
    print('E164: (+)(COUNTRY_CODE)(10_DIGIT_PHONE_NUMBER)')


def display_help():
    file = open('./helper_stuff/help.txt')
    print(file.read())
    file.close()


def exit_condition():
    sys.exit('Invalid options provided. Exiting...')
