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

    def processes(self):
        self.response = requests.get(self.url)
        self.answer = self.response.json()
        return self.answer

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
