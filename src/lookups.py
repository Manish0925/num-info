import phonenumbers
from phone_iso3166.country import phone_country
import local_lookup
import numverify_lookup
import truecaller_lookup
import phndir_lookup
import auxillary
import number_google_dorks_lookup
import name_google_dorks_lookup
from termcolor import colored


class Lookups:
    def __init__(self) -> None:
        self.truecaller_instance = None
        self.phndir_instance = None
        self.web_ui = False
        self.browser = "chrome"
        self.microsoft_details = None

    # displaying of the logo is only for the CLI, and is independent of an instance, there it has been a static method
    @staticmethod
    def display_logo():
        file = open("./helper_stuff/logo.txt", "r")
        print(colored(file.read(), "red"))
        file.close()

    # sets the webdriver (browser) to firefox or chrome
    def set_browser(self, browser):
        self.browser = browser

    # sets the web-UI to True, indicating that the user is going to use the web interface of this lookup tool
    def set_web_ui(self):
        self.web_ui = True

    # sets microsoft details via the parent program if web UI is True
    def set_microsoft_details(self, email_id, password):
        self.email_id = email_id
        self.password = password
        self.microsoft_details = (self.email_id, self.password)

    # sets the phone no. based on input
    def set_number(self, string_no):

        self.string_no = string_no
        # in case no. is entered in International format, it is converted into E164 format since the parse function can only parse E164 format nos.
        if not self.string_no.startswith("+"):
            self.string_no = "+" + self.string_no

        self.phone_no = phonenumbers.parse(self.string_no)

        if not phonenumbers.is_valid_number(self.phone_no):
            print("Invalid phone number entered. Exiting...")
            exit(-1)

        self.national_no = self.phone_no.national_number
        self.country_code = self.phone_no.country_code

    # method to handle and run all the lookup processes
    def processes(self):

        self.iso3166_code = phone_country(self.country_code)
        auxillary.line()

        # local lookup
        print("Performing Local Lookup...")
        self.local_instance = local_lookup.Local(self.string_no)
        print("Done")

        # numverify lookup (not always reliable due to server-side issues)
        print("Performing Numverify Lookup...")
        self.numverify_instance = numverify_lookup.Numverify(self.string_no)
        self.numverify_instance.processes()
        print("Done")

        # truecaller lookup (must have a microsoft account)
        if not self.web_ui:
            self.microsoft_flag = input(
                "Do you have a microsoft account? (Y/n): "
            ).lower()

        if self.microsoft_flag != "n":
            print("Performing Truecaller Lookup...")
            self.truecaller_instance = truecaller_lookup.TrueCaller(
                self.iso3166_code,
                self.national_no,
                self.browser,
                self.web_ui,
                self.microsoft_details,
            )

            # set truecaller flag to true upson successful lookup
            if self.truecaller_instance.process() != -1:
                self.truecaller_instance.set_lookup_status()
                print("Done")

        else:
            auxillary.line()
            print("Microsoft account is required for Truecaller Lookup")
            auxillary.line()

        # phndir lookup (applicable only to Indian nos.)
        if not self.web_ui:
            self.phndir_scan_flag = input(
                "Do you want to perform phndir scan? (Y/n): "
            ).lower()

        if self.phndir_scan_flag != "n":
            if self.country_code == 91:
                print("Performing Phndir Lookup...")
                self.phndir_instance = phndir_lookup.Phndir(
                    self.national_no, self.browser
                )
                if self.phndir_instance.process() != -1:
                    self.phndir_instance.set_lookup_status()
                    print("Done")
            else:
                auxillary.line()
                print("Phndir lookup only applicable to Indian nos.")
                auxillary.line()

        # google dorks number lookup
        print("Performing Google Dorks Number Lookup...")
        self.number_google_dorks_instance = (
            number_google_dorks_lookup.NumberGoogleDorksLookup(self.string_no)
        )
        print("Done")

        # google dorks name lookup (performed only if either of truecaller or phndir lookup or both succeeded)
        if (
            self.phndir_scan_flag != "n" and self.phndir_instance.get_lookup_status()
        ) or (
            self.microsoft_flag != "n" and self.truecaller_instance.get_lookup_status()
        ):
            if (
                self.microsoft_flag != "n"
                and self.truecaller_instance.get_lookup_status()
            ):
                self.person_name = self.truecaller_instance.name
            else:
                self.person_name = self.phndir_instance.caller_name

            print("Performing Google Dorks Name Lookup...")
            self.name_google_dorks_instance = (
                name_google_dorks_lookup.NameGoogleDorksLookup(self.person_name)
            )
            print("Done")

    # NOTE: name lookups are displayed if atleast Truecaller or Phndir lookups is true

    def display_results(self):

        # no need to check if the local and numverify lookups have taken place since they are guaranteed to take place

        self.local_instance.display_results(
            auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
        )

        self.numverify_instance.display_results(
            auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
        )

        # display truecaller results only if the truecaller lookup has taken place
        if self.microsoft_flag == "y" and self.truecaller_instance.get_lookup_status():
            self.truecaller_instance.display_results(
                auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
            )

        # display phndir results only if the phndir lookup has taken place
        if self.phndir_scan_flag == "y" and self.phndir_instance.get_lookup_status():
            self.phndir_instance.display_results(
                auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
            )

        # display google dorks phone number results
        self.number_google_dorks_instance.display_results(
            auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
        )

        # display google dorks phone name results (only if either of phndir or truecaller lookup has succeeded)
        if (
            self.phndir_scan_flag != "n" and self.phndir_instance.get_lookup_status()
        ) or (
            self.microsoft_flag != "n" and self.truecaller_instance.get_lookup_status()
        ):
            self.name_google_dorks_instance.display_results(
                auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
            )

    # sets the results in order to be displayed in the web-UI
    def set_results(self):
        self.local_instance.set_results()
        self.numverify_instance.set_results()
        if self.microsoft_flag != "n" and self.truecaller_instance.get_lookup_status():
            self.truecaller_instance.set_results()
        if self.phndir_scan_flag != "n" and self.phndir_instance.get_lookup_status():
            self.phndir_instance.set_results()
        self.number_google_dorks_instance.set_results()
        if (
            self.microsoft_flag != "n" and self.truecaller_instance.get_lookup_status()
        ) or (
            self.phndir_scan_flag != "n" and self.phndir_instance.get_lookup_status()
        ):
            self.name_google_dorks_instance.set_results()

    # returns the results in order to be displayed in the web-UI
    def get_results(self):

        # NOTE: the first argument passed in each of the return statements is a distinct no. which makes it easier to determine the actions to be taken
        if (
            self.microsoft_flag != "n" and self.truecaller_instance.get_lookup_status()
        ) and (
            self.phndir_scan_flag != "n" and self.phndir_instance.get_lookup_status()
        ):
            return (
                1,
                self.local_instance.get_results(),
                self.numverify_instance.get_results(),
                self.truecaller_instance.get_results(),
                self.phndir_instance.get_results(),
                self.number_google_dorks_instance.get_results(),
                self.name_google_dorks_instance.get_results(),
            )

        elif (
            not (
                self.microsoft_flag != "n"
                and self.truecaller_instance.get_lookup_status()
            )
        ) and (
            self.phndir_scan_flag != "n" and self.phndir_instance.get_lookup_status()
        ):
            return (
                2,
                self.local_instance.get_results(),
                self.numverify_instance.get_results(),
                self.phndir_instance.get_results(),
                self.number_google_dorks_instance.get_results(),
                self.name_google_dorks_instance.get_results(),
            )

        elif (
            self.microsoft_flag != "n" and self.truecaller_instance.get_lookup_status()
        ) and (
            not (
                self.phndir_scan_flag != "n"
                and self.phndir_instance.get_lookup_status()
            )
        ):
            return (
                3,
                self.local_instance.get_results(),
                self.numverify_instance.get_results(),
                self.truecaller_instance.get_results(),
                self.number_google_dorks_instance.get_results(),
                self.name_google_dorks_instance.get_results(),
            )

        else:
            return (
                4,
                self.local_instance.get_results(),
                self.numverify_instance.get_results(),
                self.number_google_dorks_instance.get_results(),
            )
