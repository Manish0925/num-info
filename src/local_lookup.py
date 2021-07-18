import phonenumbers
from phonenumbers import carrier, geocoder
from termcolor import colored
import auxillary


class Local:

    # initializes the instance attributes
    def __init__(self, phone_no) -> None:
        self.phone_no = phone_no
        self.parse_details = phonenumbers.parse(self.phone_no)
        self.national_no = phonenumbers.format_number(
            self.parse_details, phonenumbers.PhoneNumberFormat.NATIONAL
        )
        self.international_no = phonenumbers.format_number(
            self.parse_details, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        self.e164_no = phonenumbers.format_number(
            self.parse_details, phonenumbers.PhoneNumberFormat.E164
        )
        self.country_code = self.parse_details.country_code
        self.country = geocoder.description_for_number(self.parse_details, "en")
        self.carrier = carrier.name_for_number(self.parse_details, "en")

    # runs the Local lookup process
    def display_results(self, colors):
        print()
        auxillary.line()
        print(colored("Local Lookup Results:", colors[0]))
        auxillary.line()
        print(
            colored("National format     :    ", colors[1]),
            colored(self.national_no, colors[2]),
        )

        print(
            colored("E164 format         :    ", colors[1]),
            colored(self.e164_no, colors[2]),
        )

        print(
            colored("International format:    ", colors[1]),
            colored(self.international_no, colors[2]),
        )
        print(
            colored("Country Code        :    ", colors[1]),
            colored(self.country_code, colors[2]),
        )
        print(
            colored("Country             :    ", colors[1]),
            colored(self.country, colors[2]),
        )
        print(
            colored("Carrier             :    ", colors[1]),
            colored(self.carrier, colors[2]),
        )
        auxillary.line()

    # sets results to be displayed in the web-UI
    # creation of a dictionary for easier referencing
    def set_results(self):
        self.heading = "Local Lookup"
        self.dictionary = (
            {
                "Number": self.phone_no,
                "National format": self.national_no,
                "International format": self.international_no,
                "E164 format": self.e164_no,
                "Country code": self.country_code,
                "Country": self.country,
                "Carrier": self.carrier,
            },
        )

    # returns results to be displayed in the web-UI
    # NOTE: the returned value is a tuple consisting of the heading for the lookup and a dictionary (for mapping)
    def get_results(self):
        return (self.heading, self.dictionary)
