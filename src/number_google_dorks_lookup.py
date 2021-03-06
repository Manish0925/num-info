import auxillary
from termcolor import colored
from phonenumbers import parse


class NumberGoogleDorksLookup:

    # initializes the instance attributes
    def __init__(self, number) -> None:
        self.number = number

        # the given phone number needs to be parsed in order to obtain various attributes and check its validity
        self.parsed_number = parse(number)

        # list of various sites
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

    # returns links in by adding OR operators to various number formats
    # method to display results in the CLI
    def display_results(self, colors):
        print()
        auxillary.line()
        print(colored("Google Dorks Number Lookup Results:", colors[0]))
        auxillary.line()
        print(colored("General footprints", colors[1]))
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
                colors[2],
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
                colors[2],
            )
        )
        auxillary.line()
        print(colored("Social networks footprints", colors[1]))
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
            print(colored(url, colors[2]))
        auxillary.line()
        print(colored("Individual footprints", colors[1]))
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
            print(colored(url, colors[2]))
        auxillary.line()
        print(colored("Reputation footprints", colors[1]))
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
            print(colored(url, colors[2]))
        auxillary.line()
        print(colored("Temporary Sites footprints", colors[1]))
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
            print(colored(url, colors[2]))
        auxillary.line()

    # NOTE: the returned entities in each of the results are tuples which may consist of strings (or) tuples
    # NOTE: the first entity in the below tuples is the heading of the type of lookup results so that it's easy to combine them with html with the help of jinja2

    # method to set results to be displayed in the web UI
    def set_results(self):
        self.general_footprints_urls = (
            "General Footprints",
            (
                (
                    "https://www.google.com/search?q=intext%3A%22%2B"
                    + self.number[1:]
                    + "%22+OR+intext%3A%22"
                    + self.number[1:]
                    + "%22+OR+intext%3A%22"
                    + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                    + "%22"
                ),
                (
                    "intext:"
                    + '"'
                    + "+"
                    + self.number[1:]
                    + '"'
                    + " "
                    + "OR"
                    + " "
                    + "intext:"
                    + '"'
                    + self.number[1:]
                    + '"'
                    + " "
                    + "OR"
                    + " "
                    + "intext:"
                    + '"'
                    + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                    + '"'
                ),
            ),
            (
                (
                    "https://www.google.com/search?q=%28ext%3Adoc+OR+ext%3Adocx+OR+ext%3Aodt+OR+ext%3Apdf+OR+ext%3Artf+OR+ext%3Asxw+OR+ext%3Apsw+OR+ext%3Appt+OR+ext%3Apptx+OR+ext%3Apps+OR+ext%3Acsv+OR+ext%3Atxt+OR+ext%3Axls%29+intext%3A%22"
                    + self.number[1:]
                    + "%22+OR+intext%3A%22"
                    + self.number[1:]
                    + "%22+OR+intext%3A%22"
                    + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                    + "%22"
                ),
                (
                    "(ext:doc OR ext:docx OR ext:odt OR ext:pdf OR ext:rtf OR ext:sxw OR ext:psw OR ext:ppt OR ext:pptx OR ext:pps OR ext:csv OR ext:txt OR ext:xls)"
                    + " "
                    + "intext:"
                    + '"'
                    + "+"
                    + self.number[1:]
                    + '"'
                    + " "
                    + "OR"
                    + " "
                    + "intext:"
                    + '"'
                    + self.number[1:]
                    + '"'
                    + " "
                    + "OR"
                    + " "
                    + "intext:"
                    + '"'
                    + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                    + '"'
                ),
            ),
        )

        self.social_network_sites_urls = ["Social Network Footprints"]

        for i in self.social_network_sites:
            self.social_network_sites_urls.append(
                (
                    (
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
                    ),
                    (
                        "site:"
                        + i
                        + " "
                        + "intext:"
                        + '"'
                        + "+"
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                        + '"'
                    ),
                ),
            )

        self.social_network_sites_urls = tuple(self.social_network_sites_urls)

        self.individual_sites_urls = ["Individual Footprints"]

        for i in self.individual_sites:
            self.individual_sites_urls.append(
                (
                    (
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
                    ),
                    (
                        "site:" + i + " "
                        "intext:"
                        + '"'
                        + "+"
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                        + '"'
                    ),
                ),
            )

        self.individual_sites_urls = tuple(self.individual_sites_urls)

        self.reputation_sites_urls = ["Reputation Footprints"]

        for i in self.reputation_sites:
            self.reputation_sites_urls.append(
                (
                    (
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
                    ),
                    (
                        "site:" + i + " "
                        "intext:"
                        + '"'
                        + "+"
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                        + '"'
                    ),
                ),
            )

        self.reputation_sites_urls = tuple(self.reputation_sites_urls)

        self.temporary_providers_urls = ["Temporary Providers' Footprints"]

        for i in self.temporary_providers:
            self.temporary_providers_urls.append(
                (
                    (
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
                    ),
                    (
                        "site:" + i + " "
                        "intext:"
                        + '"'
                        + "+"
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[1:]
                        + '"'
                        + " "
                        + "OR"
                        + " "
                        + "intext:"
                        + '"'
                        + self.number[len(str(self.parsed_number.country_code)) + 1 :]
                        + '"'
                    ),
                ),
            )

        self.temporary_providers_urls = tuple(self.temporary_providers_urls)

        self.heading = "Number Google Dorks Lookup"

    # method to return results to be displayed in the web UI
    # NOTE: returned value is a tuple of tuples
    def get_results(self):
        return (
            self.heading,
            (
                self.general_footprints_urls,
                self.social_network_sites_urls,
                self.individual_sites_urls,
                self.reputation_sites_urls,
                self.temporary_providers_urls,
            ),
        )
