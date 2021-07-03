import requests
import auxillary
from termcolor import colored


class Numverify:
    def __init__(self, phone_no) -> None:
        # varies from account to account
        self.access_key = "f3a2feeccb645a9b89b01da28db94a8f"
        self.phone_no = phone_no

        self.url = (
            "http://apilayer.net/api/validate?access_key="
            + self.access_key
            + "&number="
            + self.phone_no
        )

    # method to handle the numverify lookup process
    def processes(self):
        self.response = requests.get(self.url)
        self.answer = self.response.json()
        return self.answer

    # sets the results to be displayed in the web-UI
    # creation of a dictionary for easier referencing
    def set_results(self):
        self.heading = "Numverify Lookup:"
        self.dictionary = (
            {
                "Number": self.answer["number"],
                "Local format": self.answer["local_format"],
                "International format": self.answer["international_format"],
                "Country prefix": self.answer["country_prefix"],
                "Country code": self.answer["country_code"],
                "Country": self.answer["country_name"],
                "Location": self.answer["location"],
                "Carrier": self.answer["carrier"],
                "Line type": self.answer["line_type"],
            },
        )

    # returns results to be displayed in the web-UI
    # NOTE: the returned value is a tuple consisting of the heading for the lookup and a dictionary (for mapping)
    def get_results(self):
        return (self.heading, self.dictionary)

    # returns results to be displayed in the CLI
    def display_results(self, color1, color2, color3):
        if self.answer["valid"]:
            print()
            auxillary.line()
            print(colored("Numverify Lookup Results:", color1))
            auxillary.line()
            print(
                colored("Number              :    ", color2),
                colored(self.answer["number"], color3),
            )
            print(
                colored("Local format        :    ", color2),
                colored(self.answer["local_format"], color3),
            )
            print(
                colored("International format:    ", color2),
                colored(self.answer["international_format"], color3),
            )
            print(
                colored("Country prefix      :    ", color2),
                colored(self.answer["country_prefix"], color3),
            )
            print(
                colored("Country code        :    ", color2),
                colored(self.answer["country_code"], color3),
            )
            print(
                colored("Country name        :    ", color2),
                colored(self.answer["country_name"], color3),
            )
            print(
                colored("Location            :    ", color2),
                colored(self.answer["location"], color3),
            )
            print(
                colored("Carrier             :    ", color2),
                colored(self.answer["carrier"], color3),
            )
            print(
                colored("Line type           :    ", color2),
                colored(self.answer["line_type"], color3),
            )
            auxillary.line()
