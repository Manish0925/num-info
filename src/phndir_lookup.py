from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from termcolor import colored
import auxillary


class Phndir:

	# initializes the instance attributes
	def __init__(self, phone_no, browser) -> None:
		self.phone_no = phone_no
		self.url = 'https://phndir.com/'
		self.browser = browser
		self.lookup_status = False

	# runs the Phndir lookup process
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
		phone_no_input = driver.find_element_by_id("phone")
		phone_no_input.send_keys(self.phone_no)
		driver.find_element_by_xpath(
			"/html/body/div[2]/div/div[2]/span/button").click()

		sleep(3)

		# condition to check if the results have loaded (since only 3 lookups a day per IP address can be performed using Phndir)
		# exiting if the first entity is not found, since that indicates search limit being exceeded
		try:
			self.caller_name = driver.find_element_by_xpath(
				"/html/body[@class='antialiased border-gray-200']/div[@id='results']/div[@class='mx-auto']/div[@class='mx-4 lg:flex max-w-6xl bg-white shadow-lg rounded-lg overflow-hidden']/div[@class='bg-white w-full lg:w-8/12 shadow overflow-hidden sm:rounded-lg']/div[@class='border-t border-gray-200']/dl/div[@class='bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6'][1]/dd[@class='mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2']").text.title()
		except NoSuchElementException:
			print('Search limit exceeded. Try again in a day or use a different IP address.')
			driver.quit()
			return -1
		self.num_type = driver.find_element_by_xpath(
			"/html/body/div[4]/div/div[1]/div[1]/div[2]/dl/div[2]/dd/span").text.upper()
		self.carrier = driver.find_element_by_xpath(
			"/html/body/div[4]/div/div[1]/div[1]/div[2]/dl/div[3]/dd").text.title()
		self.email_address = driver.find_element_by_xpath(
		    "/html/body/div[4]/div/div[1]/div[1]/div[2]/dl/div[4]/dd").text.lower()
		self.local_time = driver.find_element_by_xpath(
		    "/html/body/div[4]/div/div[1]/div[1]/div[2]/dl/div[5]/dd").text.title()

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
		print(colored('Phndir Search Results:', color1))
		auxillary.line()
		print(colored('Caller name         :    ', color2),
		      colored(self.caller_name, color3))
		print(colored('Number type         :    ', color2),
		      colored(self.num_type, color3))
		print(colored('Carrier             :    ', color2),
		      colored(self.carrier, color3))
		print(colored('Email Address       :    ', color2),
		      colored(self.email_address, color3))
		print(colored('Local Time          :    ', color2),
		      colored(self.local_time, color3))
		auxillary.line()
