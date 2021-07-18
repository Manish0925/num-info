import auxillary
from termcolor import colored


class NameGoogleDorksLookup:

    # initializes the instance attributes
    def __init__(self, name) -> None:

        # in case the username has more than one word, the spaces need to be replaced by '+' symbol, since '+' maps to space in the url
        self.name = name.replace(" ", "+")

        # list of various sites
        self.social_network_sites = (
            "facebook.com",
            "twitter.com",
            "linkedin.com",
            "instagram.com",
            "snapchat.com",
            "discord.com",
            "slack.com",
        )
        self.individual_sites = (
            "pastebin.com",
            "spytox.com",
            "locatefamily.com",
        )

    # returns links in by adding OR operators to various number formats
    # method to display results in the CLI
    def display_results(self, colors):
        print()
        auxillary.line()
        print(colored("Google Dorks Name Lookup Results:", colors[0]))
        auxillary.line()
        print(colored("General footprints", colors[1]))
        print(
            colored(
                "https://www.google.com/search?q=intext%3A%22" + self.name + "%22",
                colors[2],
            )
        )
        print(
            colored(
                "https://www.google.com/search?q=%28ext%3Adoc+OR+ext%3Adocx+OR+ext%3Aodt+OR+ext%3Apdf+OR+ext%3Artf+OR+ext%3Asxw+OR+ext%3Apsw+OR+ext%3Appt+OR+ext%3Apptx+OR+ext%3Apps+OR+ext%3Acsv+OR+ext%3Atxt+OR+ext%3Axls%29+intext%3A%22"
                + self.name
                + "%22",
                colors[2],
            )
        )
        auxillary.line()
        print(colored("Social networks footprints", colors[1]))
        for i in self.social_network_sites:
            url = (
                "https://www.google.com/search?q=site%3A"
                + i
                + "+intext%3A%22"
                + self.name
                + "%22"
            )
            print(colored(url, colors[2]))
        auxillary.line()
        print(colored("Individual footprints", colors[1]))
        for i in self.individual_sites:
            url = (
                "https://www.google.com/search?q=site%3A"
                + i
                + "+intext%3A%22"
                + self.name
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
                ("https://www.google.com/search?q=intext%3A%22" + self.name + "%22"),
                ("intext:" + '"' + self.name + '"'),
            ),
            (
                (
                    "https://www.google.com/search?q=%28ext%3Adoc+OR+ext%3Adocx+OR+ext%3Aodt+OR+ext%3Apdf+OR+ext%3Artf+OR+ext%3Asxw+OR+ext%3Apsw+OR+ext%3Appt+OR+ext%3Apptx+OR+ext%3Apps+OR+ext%3Acsv+OR+ext%3Atxt+OR+ext%3Axls%29+intext%3A%22"
                    + self.name
                    + "%22"
                ),
                (
                    "(ext:doc OR ext:docx OR ext:odt OR ext:pdf OR ext:rtf OR ext:sxw OR ext:psw OR ext:ppt OR ext:pptx OR ext:pps OR ext:csv OR ext:txt OR ext:xls)"
                    + " "
                    + "intext:"
                    + '"'
                    + self.name
                    + '"'
                ),
            ),
        )

        self.social_network_sites_urls = ["Social Network Footprints"]

        for i in self.social_network_sites:
            self.social_network_sites_urls.append(
                (
                    (
                        "https://www.google.com/search?q=site%3A"
                        + i
                        + "+intext%3A%22"
                        + self.name
                        + "%22"
                    ),
                    ("site:" + i + " " + "intext:" + '"' + self.name + '"'),
                ),
            )

        self.social_network_sites_urls = tuple(self.social_network_sites_urls)

        self.individual_sites_urls = ["Individual Sites"]

        for i in self.individual_sites:
            self.individual_sites_urls.append(
                (
                    (
                        "https://www.google.com/search?q=site%3A"
                        + i
                        + "+intext%3A%22"
                        + self.name
                        + "%22"
                    ),
                    ("site:" + i + " " + "intext:" + '"' + self.name + '"'),
                )
            )

        self.individual_sites_urls = tuple(self.individual_sites_urls)

        self.heading = "Name Google Dorks Lookup"

    # method to return results to be displayed in the web UI
    # NOTE: returned value is a tuple of tuples
    def get_results(self):
        return (
            self.heading,
            (
                self.general_footprints_urls,
                self.social_network_sites_urls,
                self.individual_sites_urls,
            ),
        )
