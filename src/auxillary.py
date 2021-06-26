import sys


def line():
    print('-----------------------------------------------------------')


def display_help():
    file = open('HELP.txt')
    print(file.read())
    file.close()


def exit_condition():
    sys.exit('Invalid options provided. Exiting...')
