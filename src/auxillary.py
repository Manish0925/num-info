import sys


def line():
    print("-----------------------------------------------------------")


def display_help():
    file = open("./helper_stuff/help.txt")
    print(file.read())
    file.close()
    sys.exit()


def exit_condition():
    sys.exit("Invalid options provided. Exiting...")
