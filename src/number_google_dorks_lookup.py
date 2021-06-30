import auxillary
from termcolor import colored
from phonenumbers import parse


class NumberGoogleDorksLookup:

    # initializes the instance attributes
    def __init__(self, number) -> None:
        self.number = number
        self.parsed_number = parse(number)
        self.social_network_sites = (
            "facebook.com",
            "twitter.com",
            "linkedin.com",
            "instagram.com",
            "vk.com",
        )
        self.individual_sites = (
            "numinfo.net",
            "sync.me",
            "whocallsyou.de",
            "pastebin.com",
            "whycall.me",
            "locatefamily.com",
            "spytox.com",
        )
        self.reputation_sites = (
            "whosenumber.info",
            "findwhocallsme.com",
            "yellowpages.ca",
            "phonenumbers.ie",
            "who-calledme.com",
            "usphonesearch.net",
            "whocalled.us",
            "quinumero.info",
            "uk.popularphotolook.com",
        )
        self.temporary_providers = (
            "hs3x.com",
            "receive-sms-now.com",
            "smslisten.com",
            "smsnumbersonline.com",
            "freesmscode.com",
            "catchsms.com",
            "smstibo.com",
            "smsreceiving.com",
            "getfreesmsnumber.com",
            "sellaite.com",
            "receive-sms-online.info",
            "receivesmsonline.com",
            "receive-a-sms.com",
            "sms-receive.net",
            "receivefreesms.com",
            "receive-sms.com",
            "receivetxt.com",
            "freephonenum.com",
            "freesmsverification.com",
            "receive-sms-online.com",
            "smslive.co",
        )

    # returns links in by adding or operators to various number formats
    def display_results(self, color1, color2, color3):
        print()
        auxillary.line()
        print(colored("Google Dorks Number Lookup Results:", color1))
        auxillary.line()
        print(colored("General footprints", color2))
        print(
            colored(
                "https://www.google.com/search?q=intext%3A%22"
                + "%2B"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext%3A%22"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext%3A%22"
                + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                + "%22",
                color3,
            )
        )
        print(
            colored(
                "https://www.google.com/search?q=%28ext%3Adoc+OR+ext%3Adocx+OR+ext%3Aodt+OR+ext%3Apdf+OR+ext%3Artf+OR+ext%3Asxw+OR+ext%3Apsw+OR+ext%3Appt+OR+ext%3Apptx+OR+ext%3Apps+OR+ext%3Acsv+OR+ext%3Atxt+OR+ext%3Axls%29+intext%3A%22"
                + "%2B"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext%3A%22"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext%3A%22"
                + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                + "%22",
                color3,
            )
        )
        auxillary.line()
        print(colored("Social networks footprints", color2))
        for i in self.social_network_sites:
            url = (
                "https://www.google.com/search?q=site"
                + "%3A"
                + i
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + "%2B"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                + "%22"
            )
            print(colored(url, color3))
        auxillary.line()
        print(colored("Individual footprints", color2))
        for i in self.individual_sites:
            url = (
                "https://www.google.com/search?q=site"
                + "%3A"
                + i
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + "%2B"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                + "%22"
            )
            print(colored(url, color3))
        auxillary.line()
        print(colored("Reputation footprints", color2))
        for i in self.reputation_sites:
            url = (
                "https://www.google.com/search?q=site"
                + "%3A"
                + i
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + "%2B"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                + "%22"
            )
            print(colored(url, color3))
        auxillary.line()
        print(colored("Temporary Sites footprints", color2))
        for i in self.temporary_providers:
            url = (
                "https://www.google.com/search?q=site"
                + "%3A"
                + i
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + "%2B"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[1:]
                + "%22"
                + "+"
                + "OR"
                + "+"
                + "intext"
                + "%3A"
                + "%22"
                + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                + "%22"
            )
            print(colored(url, color3))
        auxillary.line()
