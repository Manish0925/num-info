import sys

# colors for displaying results
colors = ("blue", "red", "green")

# line drawn to separate different entities in the CLI
def line():
    print("-----------------------------------------------------------")


# displays help page
def display_help():
    file = open("./helper_stuff/help.txt")
    print(file.read())
    file.close()
    sys.exit()


# exits the program due to invalid options
def exit_condition():
    print("Invalid options provided. Exiting...")
    sys.exit()
