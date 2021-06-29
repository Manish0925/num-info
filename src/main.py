import sys
import lookups
import auxillary

# default browser is chrome, can be set to firefox via command line args
browser = "chrome"
global person_lookups
person_lookups = None
string_no = ""


def get_person_lookups():
    return person_lookups


# sets parameters on the basis of command line args


# executes the code only if the file is being run directly (and not imported)

if len(sys.argv) == 1:

    auxillary.display_help()
    sys.exit()

elif len(sys.argv) == 2:

    if (sys.argv[1] == "-h") or (sys.argv[1] == "--help"):
        auxillary.display_help()
    else:
        auxillary.exit_condition()

elif len(sys.argv) == 3:
    if (sys.argv[1] == "-s") or (sys.argv[1] == "--scan"):
        if len(sys.argv[2]) > 10:
            string_no = sys.argv[2]
            if (
                not (string_no.startswith("+") and string_no[1:].isdigit())
                or string_no.isdigit()
            ):
                auxillary.exit_condition()
        else:
            auxillary.exit_condition()
    else:
        auxillary.exit_condition()

elif len(sys.argv) == 5:

    if (sys.argv[1] == "-b") or (sys.argv[1] == "--browser"):

        if sys.argv[2] == "firefox":
            browser = "firefox"
        elif sys.argv[2] != "chrome":
            auxillary.exit_condition()
        if (sys.argv[3] == "-s") or (sys.argv[3] == "--scan"):
            if len(sys.argv[4]) > 10:
                string_no = sys.argv[4]
                if (
                    not (string_no.startswith("+") and string_no[1:].isdigit())
                    or string_no.isdigit()
                ):
                    auxillary.exit_condition()
            else:
                auxillary.exit_condition()
        else:
            auxillary.exit_condition()

    elif (sys.argv[3] == "-b") or (sys.argv[3] == "--browser"):
        if sys.argv[4] == "firefox":
            browser = "firefox"
        elif sys.argv[4] != "chrome":
            auxillary.exit_condition()
        if (sys.argv[1] == "-s") or (sys.argv[1] == "--scan"):
            if len(sys.argv[2]) > 10:
                string_no = sys.argv[2]
                if (
                    not (string_no.startswith("+") and string_no[1:].isdigit())
                    or string_no.isdigit()
                ):
                    auxillary.exit_condition()
            else:
                auxillary.exit_condition()
        else:
            auxillary.exit_condition()

    else:
        auxillary.exit_condition()

else:
    auxillary.exit_condition()

person_lookups = lookups.Lookups()
person_lookups.set_browser(browser)
person_lookups.set_number(string_no)
person_lookups.processes()
person_lookups.display_results()

# else:
import name_google_dorks_lookup

user_name = None
user_email_id = None
user_phone_no = (
    "+"
    + str(person_lookups.local_instance.country_code)
    + str(person_lookups.local_instance.national_no)
)

if (
    person_lookups.country_code == 91
    and person_lookups.phndir_scan_flag.lower() == "y"
    and person_lookups.phndir_instance.get_lookup_status()
):
    user_name = person_lookups.phndir_instance.caller_name
    user_email_id = person_lookups.phndir_instance.email_address

if (
    person_lookups.microsoft_flag.lower() == "y"
    and person_lookups.truecaller_instance.get_lookup_status()
):
    user_name = person_lookups.truecaller_instance.name
    user_email_id = person_lookups.truecaller_instance.email_id

if user_name != None:
    name_google_dorks_lookup_instance = name_google_dorks_lookup.NameGoogleDorksLookup(
        user_name
    )
    name_google_dorks_lookup_instance.display_results(
        auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
    )
