import auxillary
from termcolor import colored


class NameGoogleDorksLookup:
    def __init__(self, name) -> None:
        self.name = name
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

    def display_results(self, color1, color2, color3):
        j = self.name.split()
        if len(j) > 1:
            self.name = ""
            for k in range(len(j) - 1):
                self.name += j[k]
                self.name += "+"
            self.name += j[len(j) - 1]
        auxillary.line()
        print(colored("Google Dorks Name Lookup Results:", color1))
        auxillary.line()
        print(colored("General footprints", color2))
        print(
            colored(
                "https://www.google.com/search?q=intext%3A%22" + self.name + "%22",
                color3,
            )
        )
        print(
            colored(
                "https://www.google.com/search?q=%28ext%3Adoc+OR+ext%3Adocx+OR+ext%3Aodt+OR+ext%3Apdf+OR+ext%3Artf+OR+ext%3Asxw+OR+ext%3Apsw+OR+ext%3Appt+OR+ext%3Apptx+OR+ext%3Apps+OR+ext%3Acsv+OR+ext%3Atxt+OR+ext%3Axls%29+intext%3A%22"
                + self.name
                + "%22",
                color3,
            )
        )
        auxillary.line()
        print(colored("Social networks footprints", color2))
        for i in self.social_network_sites:
            url = (
                "https://www.google.com/search?q=site%3A"
                + i
                + "+intext%3A%22"
                + self.name
                + "%22"
            )
            print(colored(url, color3))
        auxillary.line()
        print(colored("Individual footprints", color2))
        for i in self.individual_sites:
            url = (
                "https://www.google.com/search?q=site%3A"
                + i
                + "+intext%3A%22"
                + self.name
                + "%22"
            )
            print(colored(url, color3))
        auxillary.line()
