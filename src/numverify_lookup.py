import requests
import auxillary
from termcolor import colored


class Numverify:
    def __init__(self, phone_no) -> None:
        # varies from account to account
        self.access_key = "f3a2feeccb645a9b89b01da28db94a8f"
        self.phone_no = phone_no
        self.lookup_status = False

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
        try:
            self.answer["valid"]
        except KeyError:
            return -1
        self.heading = "Numverify Lookup"
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
        return 0

    def set_lookup_status(self):
        self.lookup_status = True

    def get_lookup_status(self):
        return self.lookup_status

    # returns results to be displayed in the web-UI
    # NOTE: the returned value is a tuple consisting of the heading for the lookup and a dictionary (for mapping)
    def get_results(self):
        return (self.heading, self.dictionary)

    # returns results to be displayed in the CLI
    def display_results(self, colors):
        try:
            self.answer["valid"]
        except KeyError:
            return -1
        if self.answer["valid"]:
            print()
            auxillary.line()
            print(colored("Numverify Lookup Results:", colors[0]))
            auxillary.line()
            print(
                colored("Number              :    ", colors[1]),
                colored(self.answer["number"], colors[2]),
            )
            print(
                colored("Local format        :    ", colors[1]),
                colored(self.answer["local_format"], colors[2]),
            )
            print(
                colored("International format:    ", colors[1]),
                colored(self.answer["international_format"], colors[2]),
            )
            print(
                colored("Country prefix      :    ", colors[1]),
                colored(self.answer["country_prefix"], colors[2]),
            )
            print(
                colored("Country code        :    ", colors[1]),
                colored(self.answer["country_code"], colors[2]),
            )
            print(
                colored("Country name        :    ", colors[1]),
                colored(self.answer["country_name"], colors[2]),
            )
            print(
                colored("Location            :    ", colors[1]),
                colored(self.answer["location"], colors[2]),
            )
            print(
                colored("Carrier             :    ", colors[1]),
                colored(self.answer["carrier"], colors[2]),
            )
            print(
                colored("Line type           :    ", colors[1]),
                colored(self.answer["line_type"], colors[2]),
            )
            auxillary.line()

        return 0
