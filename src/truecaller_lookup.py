from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from getpass import getpass
from termcolor import colored
import auxillary


class TrueCaller:

    # initializes the instance attributes
    def __init__(
        self, iso3166_code, phone_no, browser, web_ui, microsoft_details
    ) -> None:
        self.iso3166_code = iso3166_code
        self.phone_no = phone_no
        self.url = (
            "https://www.truecaller.com/search/" + iso3166_code + "/" + str(phone_no)
        )
        self.browser = browser
        self.lookup_status = False
        self.web_ui = web_ui
        if self.web_ui:
            self.your_email_id = microsoft_details[0]
            self.your_password = microsoft_details[1]
        else:
            self.your_email_id = None
            self.your_password = None

    # runs the Truecaller lookup process
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
            # options.add_argument("headless")
            options.add_argument("log-level=3")
            driver = webdriver.Chrome(options=options)

        # the URL is provided which the webdriver opens in the browser (in the background)
        driver.get(self.url)

        # NOTE: sleep functions are in order to ensure that the webpage gets fully loaded
        sleep(3)

        # NOTE: the elements in the webpage are either found with the help of their xpath
        microsoft_sign_in = driver.find_element_by_xpath('//*[@id="app"]/main/div/a[2]')
        microsoft_sign_in.click()

        if not self.web_ui:
            sleep(3)
            print()
            auxillary.line()
            print(
                "Personal details required for enabling the required services\nNOTE: Details aren't stored"
            )
            auxillary.line()
            print()

            # signing in with microsoft account was the only option since google didn't allow signing-in due to security reasons
            print("Microsoft Details:")
            self.your_email_id = input("Email-ID            :    ")
            self.your_password = getpass(prompt="Password            :    ")

        sleep(3)
        your_email_id_input = driver.find_element_by_xpath('//*[@id="i0116"]')
        your_email_id_input.send_keys(self.your_email_id, Keys.RETURN)

        sleep(4)

        security = driver.find_elements_by_xpath('//*[@id="idA_PWD_SwitchToCredPicker"]')
        if len(security) != 0:
            security[0].click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="credentialList"]/div[3]/div/div/div[2]').click()

        sleep(2)

        your_password_input = driver.find_element_by_xpath('//*[@id="i0118"]')
        your_password_input.send_keys(self.your_password, Keys.RETURN)

        sleep(6)

        # condition to check if the results have loaded (since only 3 lookups a day per IP address can be performed using Phndir)
        # exiting if the first entity is not found, since that indicates search limit being exceeded
        try:
            self.name = driver.find_element_by_xpath(
                '//*[@id="app"]/main/div/div[1]/div[1]/header/div[2]/h1/span'
            ).text.title()
        except NoSuchElementException:
            print("Issue could be one among the following:")
            print("- Incorrect username\n- Incorrect password")
            print(
                "- Search limit exceeded. Try again in a day or use a different microsoft account."
            )
            driver.quit()
            return -1
        self.email_id = driver.find_element_by_xpath(
            '//*[@id="app"]/main/div/div[1]/div[2]/a[2]/div'
        ).text.lower()
        self.service_provider = driver.find_element_by_xpath(
            '//*[@id="app"]/main/div/div[1]/div[2]/a[1]/div/div[2]'
        ).text.title()
        self.local_time = driver.find_element_by_xpath(
            '//*[@id="app"]/main/div/div[1]/div[2]/a[3]/div/div[2]'
        ).text.title()
        self.location = driver.find_element_by_xpath(
            '//*[@id="app"]/main/div/div[1]/div[2]/a[3]/div/div[1]'
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
        self.heading = "Truecaller Lookup"
        self.dictionary = (
            {
                "Name": self.name,
                "Email address": self.email_id,
                "Service Provider": self.service_provider,
                "Local time": self.local_time,
                "Location": self.location,
            },
        )

    # returns the results in order to be displayed in the web UI
    # NOTE: the returned value is a tuple consisting of the heading for the lookup and a dictionary (for mapping)
    def get_results(self):
        return (self.heading, self.dictionary)

    # displays results in the CLI
    def display_results(self, colors):
        print()
        auxillary.line()
        print(colored("Truecaller Lookup Results:", colors[0]))
        auxillary.line()
        print(
            colored("Name                :    ", colors[1]),
            colored(self.name, colors[2]),
        )
        print(
            colored("Email-ID            :    ", colors[1]),
            colored(self.email_id, colors[2]),
        )
        print(
            colored("Service Provider    :    ", colors[1]),
            colored(self.service_provider, colors[2]),
        )
        print(
            colored("Local Time          :    ", colors[1]),
            colored(self.local_time, colors[2]),
        )
        print(
            colored("Location            :    ", colors[1]),
            colored(self.location, colors[2]),
        )
        auxillary.line()
