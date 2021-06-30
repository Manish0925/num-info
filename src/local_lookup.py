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
    def display_results(self, color1, color2, color3):
        print()
        auxillary.line()
        print(colored("Local Lookup Results:", color1))
        auxillary.line()
        print(
            colored("National format     :    ", color2),
            colored(self.national_no, color3),
        )

        print(
            colored("E164 format         :    ", color2), colored(self.e164_no, color3)
        )

        print(
            colored("International format:    ", color2),
            colored(self.international_no, color3),
        )
        print(
            colored("Country Code        :    ", color2),
            colored(self.country_code, color3),
        )
        print(
            colored("Country             :    ", color2), colored(self.country, color3)
        )
        print(
            colored("Carrier             :    ", color2), colored(self.carrier, color3)
        )
        auxillary.line()
