import sys

# colors for displaying results
colors = ("blue", "red", "green")


def line():
    print("-----------------------------------------------------------")


def display_help():
    file = open("./helper_stuff/help.txt")
    print(file.read())
    file.close()
    sys.exit()


def exit_condition():
    print("Invalid options provided. Exiting...")
    sys.exit()
