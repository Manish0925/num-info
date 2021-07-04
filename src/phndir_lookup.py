from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from termcolor import colored
import auxillary


class Phndir:

    # initializes the instance attributes
    def __init__(self, phone_no, browser) -> None:
        self.phone_no = phone_no
        self.url = "https://phndir.com/"
        self.browser = browser
        self.lookup_status = False

    # runs the Phndir lookup process
    def process(self):

        # checks if browser is firefox or chrome
        # headless argument is to prevent the browser from being displayed
        # log-level=3 argument is to prevent warning messages from being displayed on the console
        if self.browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.set_headless()
            options.add_argument("log-level=3")
            driver = webdriver.Firefox(options=options)
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            options.add_argument("log-level=3")
            driver = webdriver.Chrome(options=options)

        # the URL is provided which the webdriver opens in the browser (in the background)
        driver.get(self.url)

        # NOTE: sleep functions are in order to ensure that the webpage gets fully loaded
        sleep(2)

        # NOTE: the elements in the webpage are either found with the help of their id (or) xpath
        # phone_no_input = driver.find_element_by_id("phone")
        phone_no_input = driver.find_element_by_xpath('//*[@id="phone"]')
        phone_no_input.send_keys(self.phone_no)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/span/button").click()
        driver.find_element_by_xpath('//*[@id="query"]/span/button').click()

        sleep(3)

        # condition to check if the results have loaded (since only 3 lookups a day per IP address can be performed using Phndir)
        # exiting if the first entity is not found, since that indicates search limit being exceeded
        try:
            self.caller_name = driver.find_element_by_xpath(
                '//*[@id="results"]/div/div[1]/div[1]/div[2]/dl/div[1]/dd'
            ).text.title()
        except NoSuchElementException:
            auxillary.line()
            print(
                "Search limit exceeded. Try again in a day or use a different IP address."
            )
            auxillary.line()
            driver.quit()
            return -1
        self.num_type = driver.find_element_by_xpath(
            '//*[@id="results"]/div/div[1]/div[1]/div[2]/dl/div[2]/dd/span'
        ).text.upper()
        self.carrier = driver.find_element_by_xpath(
            '//*[@id="results"]/div/div[1]/div[1]/div[2]/dl/div[3]/dd'
        ).text.title()
        self.email_address = driver.find_element_by_xpath(
            '//*[@id="results"]/div/div[1]/div[1]/div[2]/dl/div[4]/dd'
        ).text.lower()
        self.local_time = driver.find_element_by_xpath(
            '//*[@id="results"]/div/div[1]/div[1]/div[2]/dl/div[5]/dd'
        ).text.title()

        # quits the browser
        driver.quit()

        return 0

    # sets the lookup value to true, indicating that the lookup has taken place
    def set_lookup_status(self):
        self.lookup_status = True

    # returns if or not the lookup has taken place
    def get_lookup_status(self):
        return self.lookup_status

    # sets the results in order to be displayed in the web UI
    # creation of a dictionary for easier referencing
    def set_results(self):
        self.heading = "Phndir Lookup"
        self.dictionary = (
            {
                "Name": self.caller_name,
                "Number type": self.num_type,
                "Carrier": self.carrier,
                "Email address": self.email_address,
                "Local time": self.local_time,
            },
        )

    # returns the results in order to be displayed in the web UI
    # NOTE: the returned value is a tuple consisting of the heading for the lookup and a dictionary (for mapping)
    def get_results(self):
        return (self.heading, self.dictionary)

    # displays results in the CLI
    def display_results(self, color1, color2, color3):
        print()
        auxillary.line()
        print(colored("Phndir Lookup Results:", color1))
        auxillary.line()
        print(
            colored("Caller name         :    ", color2),
            colored(self.caller_name, color3),
        )
        print(
            colored("Number type         :    ", color2), colored(self.num_type, color3)
        )
        print(
            colored("Carrier             :    ", color2), colored(self.carrier, color3)
        )
        print(
            colored("Email Address       :    ", color2),
            colored(self.email_address, color3),
        )
        print(
            colored("Local Time          :    ", color2),
            colored(self.local_time, color3),
        )
        auxillary.line()
