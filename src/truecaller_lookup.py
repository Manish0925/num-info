from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from getpass import getpass
from termcolor import colored
from auxillary import line


class TrueCaller:

	def __init__(self, iso3166_code, phone_no, browser) -> None:
		self.iso3166_code = iso3166_code
		self.phone_no = phone_no
		self.url = 'https://www.truecaller.com/search/' + \
			iso3166_code + '/' + str(phone_no)
		self.browser = browser

	def process(self):
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
		driver.get(self.url)
		sleep(2)
		microsoft_sign_in = driver.find_element_by_xpath(
		    "/html/body/div[1]/main/div/a[2]"
		)
		microsoft_sign_in.click()
		sleep(2)
		line()
		print('Personal details required for enabling the required services\nNOTE: Details aren\'t stored')
		line()
		print('Microsoft Details:')
		self.your_email_id = input('Email-ID            :    ')
		self.your_password = getpass(prompt='Password            :    ')
		your_email_id_input = driver.find_element_by_id('i0116')
		your_email_id_input.send_keys(self.your_email_id, Keys.RETURN)
		sleep(4)
		your_password_input = driver.find_element_by_id('i0118')
		your_password_input.send_keys(self.your_password, Keys.RETURN)
		sleep(6)
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
		driver.quit()
		return 0

	def display_results(self, color1, color2, color3):
		print()
		line()
		print(colored('Truecaller Search Results:', color1))
		line()
		print(colored('Name                :    ', color2), colored(self.name, color3))
		print(colored('Email-ID            :    ', color2),
		      colored(self.email_id, color3))
		print(colored('Service Provider    :    ', color2),
		      colored(self.service_provider, color3))
		print(colored('Local Time          :    ', color2),
		      colored(self.local_time, color3))
		print(colored('Location            :    ', color2),
		      colored(self.location, color3))
		line()
