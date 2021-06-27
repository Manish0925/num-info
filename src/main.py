from lookups import Lookups
import sys
import auxillary

# default browser
browser = 'chrome'

if len(sys.argv) == 1:
	auxillary.display_help()
	sys.exit()
elif len(sys.argv) == 2:
	if (sys.argv[1] == '-h') or (sys.argv[1] == '--help'):
		auxillary.display_help()
	elif (sys.argv[1] == '-s') or (sys.argv[1] == '--scan'):
		pass
	else:
		auxillary.exit_condition()
elif len(sys.argv) == 4:
	if (sys.argv[1] == '-b') or (sys.argv[1] == '--browser'):
		if (sys.argv[2] == 'firefox'):
			browser = 'firefox'
		elif (sys.argv[2] != 'chrome'):
			auxillary.exit_condition()
		if (sys.argv[3] == '-s') or (sys.argv[3] == '--scan'):
			pass
	elif (sys.argv[1] == '-s') or (sys.argv[1] == '--scan'):
		if not (sys.argv[2] == '-b') or (sys.argv[2] == '--browser'):
			auxillary.exit_condition()
		if (sys.argv[3] == 'firefox'):
			browser = 'firefox'
		elif (sys.argv[3] != 'chrome'):
			auxillary.exit_condition()
	else:
		auxillary.exit_condition()
else:
	auxillary.exit_condition()

if __name__ == '__main__':
	lookups = Lookups()
	lookups.set_browser(browser)
	lookups.set_number()
	lookups.processes()
