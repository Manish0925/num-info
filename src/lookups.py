import sys
import phonenumbers
from phone_iso3166.country import phone_country
import local_lookup
import numverify_lookup
import truecaller_lookup
import phndir_lookup
import auxillary


class Lookups:
    def __init__(self) -> None:
        self.truecaller_instance = None
        self.phndir_instance = None

    # sets the webdriver (browser) to firefox or chrome
    def set_browser(self, browser):
        self.browser = browser

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

        # # numverify lookup (not always reliable due to server-side issues)
        # print("Performing Numverify Lookup...")
        # self.numverify_instance = numverify_lookup.Numverify(self.string_no)
        # self.numverify_instance.processes()
        # print("Done")

        # truecaller lookup (must have a microsoft account)
        self.microsoft_flag = input("Do you have a microsoft account? (Y/n): ").lower()

        if self.microsoft_flag != "n":
            print("Performing Truecaller Lookup...")
            self.truecaller_instance = truecaller_lookup.TrueCaller(
                self.iso3166_code, self.national_no, self.browser
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

    def display_results(self):

        # no need to check if the local and numverify lookups have taken place since they are guaranteed to take place

        self.local_instance.display_results(
            auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
        )

        # self.numverify_instance.display_results(
        #     auxillary.colors[0], auxillary.colors[1], auxillary.colors[2]
        # )

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
