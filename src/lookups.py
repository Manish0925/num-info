import phonenumbers
from truecaller_search import TrueCaller
from phone_iso3166.country import phone_country
from phndir_search import Phndir
from auxillary import line


class Lookups:

	def __init__(self) -> None:
		pass

	def set_browser(self, browser):
		self.browser = browser

	def set_number(self):
		line()
		print('International (COUNTRY_CODE)(10_DIGIT_PHONE_NUMBER)')
		print('or')
		print('E164 (+)(COUNTRY_CODE)(10_DIGIT_PHONE_NUMBER)')
		line()
		string_no = input('Enter here          :    ')
		if not string_no.startswith('+'):
			string_no = '+'+string_no
		self.phone_no = phonenumbers.parse(string_no)
		while not phonenumbers.is_valid_number(self.phone_no):
			line()
			print('Enter valid nuber')
			line()
			string_no = input('Enter here          :    ')
			if not string_no.startswith('+'):
				string_no = '+'+string_no
			self.phone_no = phonenumbers.parse(string_no)
		self.national_no = self.phone_no.national_number
		self.country_code = self.phone_no.country_code

	def processes(self):
		colors = ('blue', 'red', 'green')
		# truecaller lookup
		self.iso3166_code = phone_country(self.country_code)
		truecaller_instance = TrueCaller(
			self.iso3166_code, self.national_no, self.browser)
		if truecaller_instance.process() != -1:
			truecaller_instance.display_results(colors[0], colors[1], colors[2])
		if self.country_code == 91:
			# phndir lookup (applicable only to Indian nos.)
			phndir_instance = Phndir(self.national_no, self.browser)
			if phndir_instance.process() != -1:
				phndir_instance.display_results(colors[0], colors[1], colors[2])
