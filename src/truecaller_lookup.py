from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from getpass import getpass
from termcolor import colored
import auxillary


class TrueCaller:

	# initializes the instance attributes
	def __init__(self, iso3166_code, phone_no, browser) -> None:
		self.iso3166_code = iso3166_code
		self.phone_no = phone_no
		self.url = 'https://www.truecaller.com/search/' + \
			iso3166_code + '/' + str(phone_no)
		self.browser = browser
		self.lookup_status = False

	# runs the Truecaller lookup process
	def process(self):

		# checks if browser is firefox or chrome
		# headless argument is to prevent the browser from being displayed
		# log-level=3 argument is to prevent warning messages from being displayed on the console
		if self.browser == 'firefox':
			options = webdriver.FirefoxOptions()
			options.set_headless()
			options.add_argument('log-level=3')
			driver = webdriver.Firefox(options=options)
		else:
			options = webdriver.ChromeOptions()
			options.add_argument('headless')
			options.add_argument('log-level=3')
			driver = webdriver.Chrome(options=options)

		# the URL is provided which the webdriver opens in the browser (in the background)
		driver.get(self.url)

		# NOTE: sleep functions are in order to ensure that the webpage gets fully loaded
		sleep(2)

		# NOTE: the elements in the webpage are either found with the help of their id (or) xpath
		microsoft_sign_in = driver.find_element_by_xpath(
		    "/html/body/div[1]/main/div/a[2]"
		)
		microsoft_sign_in.click()
		sleep(2)
		auxillary.line()
		print('Personal details required for enabling the required services\nNOTE: Details aren\'t stored')
		auxillary.line()

		# signing in with microsoft account was the only option since google didn't allow signing-in due to security reasons
		print('Microsoft Details:')
		self.your_email_id = input('Email-ID            :    ')
		self.your_password = getpass(prompt='Password            :    ')
		your_email_id_input = driver.find_element_by_id('i0116')
		your_email_id_input.send_keys(self.your_email_id, Keys.RETURN)

		sleep(4)

		your_password_input = driver.find_element_by_id('i0118')
		your_password_input.send_keys(self.your_password, Keys.RETURN)

		sleep(6)

		# condition to check if the results have loaded (since only 3 lookups a day per IP address can be performed using Phndir)
		# exiting if the first entity is not found, since that indicates search limit being exceeded
		try:
			self.name = driver.find_element_by_xpath(
				"/html/body/div[1]/main/div/div[1]/div[1]/header/div[2]/h1/span").text.title()
		except NoSuchElementException:
			print('Search limit exceeded. Try again in a day or use a different microsoft account.')
			driver.quit()
			return -1
		self.email_id = driver.find_element_by_xpath(
			"/html/body/div[1]/main/div/div[1]/div[2]/a[2]/div").text.lower()
		self.service_provider = driver.find_element_by_xpath(
		    "/html/body/div[1]/main/div/div[1]/div[2]/a[1]/div/div[2]").text.title()
		self.local_time = driver.find_element_by_xpath(
		    "/html/body/div[1]/main/div/div[1]/div[2]/a[3]/div/div[2]").text.title()
		self.location = driver.find_element_by_xpath(
		    "/html/body/div[1]/main/div/div[1]/div[2]/a[3]/div/div[1]").text.title()

		# quits the browser
		driver.quit()
		return 0

	def set_lookup_status(self):
		self.lookup_status = True

	def get_lookup_status(self):
		return self.lookup_status

	def display_results(self, color1, color2, color3):
		print()
		auxillary.line()
		print(colored('Truecaller Search Results:', color1))
		auxillary.line()
		print(colored('Name                :    ', color2), colored(self.name, color3))
		print(colored('Email-ID            :    ', color2),
		      colored(self.email_id, color3))
		print(colored('Service Provider    :    ', color2),
		      colored(self.service_provider, color3))
		print(colored('Local Time          :    ', color2),
		      colored(self.local_time, color3))
		print(colored('Location            :    ', color2),
		      colored(self.location, color3))
		auxillary.line()